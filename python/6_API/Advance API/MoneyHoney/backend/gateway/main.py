import os
import sys
import uuid
import time
import logging
from pathlib import Path
from typing import Set

import jwt
import httpx
from fastapi import FastAPI, Request, Response, HTTPException, status
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.gateway.rate_limiter import SlidingWindowRateLimiter

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] [GATEWAY] %(message)s")
logger = logging.getLogger("moneyhoney.gateway")

# Microservice Targets
AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://127.0.0.1:8001").rstrip("/")
TRADES_SERVICE_URL = os.getenv("TRADES_SERVICE_URL", "http://127.0.0.1:8002").rstrip("/")
USERS_SERVICE_URL = os.getenv("USERS_SERVICE_URL", "http://127.0.0.1:8003").rstrip("/")

SECRET_KEY = os.getenv("SECRET_KEY", "change-this-to-a-secure-random-secret-key-in-prod")
ALGORITHM = "HS256"
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# Rate limit thresholds (requests per minute)
RATE_LIMIT_ANONYMOUS = int(os.getenv("RATE_LIMIT_ANON", 60))
RATE_LIMIT_AUTHENTICATED = int(os.getenv("RATE_LIMIT_AUTH", 180))
RATE_LIMIT_LOGIN = int(os.getenv("RATE_LIMIT_LOGIN", 10))

# Publicly accessible routes that bypass mandatory JWT verification
PUBLIC_PATHS: Set[str] = {
    "/health",
    "/mh/v1/login",
    "/login",
    "/mh/v1/refresh",
    "/refresh",
    "/docs",
    "/openapi.json",
    "/redoc"
}

def resolve_microservice(path: str):
    """
    Route requests to the appropriate microservice based on URL path.
    Returns: (target_base_url, service_name)
    """
    clean_path = path.lower()
    
    # 1. Auth Microservice: Authentication & Tokens
    if any(clean_path.startswith(p) for p in ["/login", "/refresh", "/mh/v1/login", "/mh/v1/refresh"]):
        return AUTH_SERVICE_URL, "Auth Microservice"

    # 2. Trades Microservice: Orders & Trade History
    if any(clean_path.startswith(p) for p in ["/trade", "/mytrades", "/mh/v1/trade", "/mh/v1/mytrades"]):
        return TRADES_SERVICE_URL, "Trades Microservice"

    # 3. Users & Market Data Microservice: Ticker minute data, Watchlists & Health
    return USERS_SERVICE_URL, "Users/Market Data Microservice"


# Hop-by-hop headers that should not be forwarded
HOP_BY_HOP_HEADERS = {
    "connection",
    "keep-alive",
    "proxy-authenticate",
    "proxy-authorization",
    "te",
    "trailers",
    "transfer-encoding",
    "upgrade",
    "content-length"
}

# Initialize Gateway Application & Rate Limiter
app = FastAPI(
    title="MoneyHoney API Gateway",
    description="Edge API Gateway: Central Authentication, Rate Limiting, Request Tracking & Routing",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rate_limiter = SlidingWindowRateLimiter(redis_host=REDIS_HOST, redis_port=REDIS_PORT)

# Reusable AsyncClient with connection pooling
http_client: httpx.AsyncClient = None

def get_http_client() -> httpx.AsyncClient:
    global http_client
    if http_client is None or http_client.is_closed:
        http_client = httpx.AsyncClient(
            timeout=httpx.Timeout(connect=5.0, read=30.0, write=10.0, pool=30.0),
            limits=httpx.Limits(max_keepalive_connections=150, max_connections=300)
        )
    return http_client

@app.on_event("startup")
async def startup_event():
    get_http_client()
    logger.info("API Gateway started on port 8000.")
    logger.info(f"  -> Auth Service:   {AUTH_SERVICE_URL}")
    logger.info(f"  -> Trades Service: {TRADES_SERVICE_URL}")
    logger.info(f"  -> Users Service:  {USERS_SERVICE_URL}")

@app.on_event("shutdown")
async def shutdown_event():
    global http_client
    if http_client and not http_client.is_closed:
        await http_client.aclose()
        logger.info("API Gateway HTTP client connection pool closed.")


@app.get("/health", tags=["Gateway Health"])
async def gateway_health():
    """Health check endpoint checking gateway status and downstream microservices."""
    client = get_http_client()
    services_status = {}

    for name, url in [("auth", AUTH_SERVICE_URL), ("trades", TRADES_SERVICE_URL), ("users", USERS_SERVICE_URL)]:
        try:
            resp = await client.get(f"{url}/mh/v1/home", timeout=1.0)
            services_status[name] = "healthy" if resp.status_code == 200 else f"status {resp.status_code}"
        except Exception:
            try:
                resp = await client.get(f"{url}/health", timeout=1.0)
                services_status[name] = "healthy" if resp.status_code == 200 else f"status {resp.status_code}"
            except Exception as exc:
                services_status[name] = f"offline ({str(exc)})"

    return {
        "gateway_status": "healthy",
        "redis_connected": rate_limiter.redis_client is not None,
        "downstream_services": {
            "auth_service": AUTH_SERVICE_URL,
            "trades_service": TRADES_SERVICE_URL,
            "users_service": USERS_SERVICE_URL
        },
        "services_health": services_status,
        "timestamp": time.time()
    }


@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"])
async def gateway_proxy(request: Request, path: str):
    """
    Central Gateway handler:
    1. Injects correlation tracking (X-Request-ID).
    2. Applies Rate Limiting (per IP or User ID).
    3. Enforces JWT Authentication on non-public endpoints.
    4. Routes request to the respective microservice by path.
    """
    req_start = time.perf_counter()
    full_path = f"/{path}"

    # 1. Correlation tracking
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    client_ip = request.client.host if request.client else "unknown"

    # 2. Authentication check & user extraction
    auth_header = request.headers.get("Authorization")
    user_payload = None
    user_id = None
    auth_error_detail = None
    auth_error_code = "UNAUTHORIZED"

    if not auth_header:
        auth_error_detail = "Authorization header missing. Bearer access token required."
    elif not auth_header.startswith("Bearer "):
        auth_error_detail = "Invalid Authorization header format. Expected 'Bearer <token>'."
    else:
        token = auth_header.split(" ", 1)[1].strip()
        try:
            user_payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            if user_payload.get("type") != "access":
                auth_error_detail = "Invalid token type: access token required (received refresh or invalid token)."
                auth_error_code = "INVALID_TOKEN_TYPE"
                user_payload = None
            else:
                user_id = user_payload.get("sub")
        except jwt.ExpiredSignatureError:
            auth_error_detail = "Access token expired. Please refresh your token or log in again."
            auth_error_code = "TOKEN_EXPIRED"
            user_payload = None
        except jwt.InvalidTokenError:
            auth_error_detail = "Invalid or corrupted access token."
            auth_error_code = "INVALID_TOKEN"
            user_payload = None
        except Exception as exc:
            auth_error_detail = f"Token validation error: {str(exc)}"
            auth_error_code = "AUTH_ERROR"
            user_payload = None

    # Enforce authentication if route is not public
    is_public = any(full_path.startswith(pub) for pub in PUBLIC_PATHS)
    if not is_public and user_payload is None:
        logger.warning(f"[{request_id}] Unauthorized request to {full_path} from {client_ip}: {auth_error_detail}")
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "error": "Unauthorized",
                "code": auth_error_code,
                "detail": auth_error_detail or "Valid Bearer access token required to access this endpoint",
                "request_id": request_id
            },
            headers={"WWW-Authenticate": f'Bearer error="{auth_error_code.lower()}", error_description="{auth_error_detail}"', "X-Request-ID": request_id}
        )

    # 3. Rate Limiting check
    if full_path.endswith("/login"):
        rate_id = f"ip:{client_ip}:login"
        rate_limit = RATE_LIMIT_LOGIN
    elif user_id:
        rate_id = f"user:{user_id}"
        rate_limit = RATE_LIMIT_AUTHENTICATED
    else:
        rate_id = f"ip:{client_ip}"
        rate_limit = RATE_LIMIT_ANONYMOUS

    is_limited, remaining, retry_after = rate_limiter.is_rate_limited(
        identifier=rate_id,
        limit=rate_limit,
        window_seconds=60
    )

    if is_limited:
        logger.warning(f"[{request_id}] Rate limit exceeded for {rate_id} on {full_path}")
        return JSONResponse(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            content={
                "error": "Too Many Requests",
                "detail": f"Rate limit of {rate_limit} req/min exceeded. Please slow down.",
                "retry_after": retry_after,
                "request_id": request_id
            },
            headers={
                "Retry-After": str(retry_after),
                "X-RateLimit-Limit": str(rate_limit),
                "X-RateLimit-Remaining": "0",
                "X-RateLimit-Reset": str(retry_after),
                "X-Request-ID": request_id
            }
        )

    # 4. Resolve microservice destination by path
    target_base, service_name = resolve_microservice(full_path)
    target_url = f"{target_base}{full_path}"
    if request.url.query:
        target_url = f"{target_url}?{request.url.query}"

    # Filter hop-by-hop headers
    forward_headers = {
        k: v for k, v in request.headers.items()
        if k.lower() not in HOP_BY_HOP_HEADERS and k.lower() != "host"
    }
    forward_headers["X-Request-ID"] = request_id
    forward_headers["X-Forwarded-For"] = client_ip
    if user_id:
        forward_headers["X-Authenticated-User"] = str(user_id)

    # Forward body
    body = await request.body()

    try:
        client = get_http_client()
        upstream_req = client.build_request(
            method=request.method,
            url=target_url,
            headers=forward_headers,
            content=body
        )
        upstream_resp = await client.send(upstream_req, stream=True)

        # Build response headers
        resp_headers = {
            k: v for k, v in upstream_resp.headers.items()
            if k.lower() not in HOP_BY_HOP_HEADERS
        }
        resp_headers["X-Request-ID"] = request_id
        resp_headers["X-RateLimit-Limit"] = str(rate_limit)
        resp_headers["X-RateLimit-Remaining"] = str(remaining)
        resp_headers["X-Gateway-Latency-Ms"] = f"{(time.perf_counter() - req_start) * 1000:.2f}"
        resp_headers["X-Routed-Microservice"] = service_name
        resp_headers["X-Microservice-URL"] = target_base

        # Stream upstream response back to client
        return StreamingResponse(
            upstream_resp.aiter_raw(),
            status_code=upstream_resp.status_code,
            headers=resp_headers,
            background=upstream_resp.aclose
        )

    except httpx.ConnectError:
        logger.error(f"[{request_id}] Connection refused from {service_name} at {target_base}")
        return JSONResponse(
            status_code=status.HTTP_502_BAD_GATEWAY,
            content={
                "error": "Bad Gateway",
                "detail": f"{service_name} is unreachable at {target_base}.",
                "microservice": service_name,
                "target_url": target_base,
                "request_id": request_id
            },
            headers={"X-Request-ID": request_id}
        )
    except httpx.TimeoutException:
        logger.error(f"[{request_id}] Request to {full_path} timed out on {service_name}")
        return JSONResponse(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            content={
                "error": "Gateway Timeout",
                "detail": f"{service_name} timed out.",
                "microservice": service_name,
                "request_id": request_id
            },
            headers={"X-Request-ID": request_id}
        )

    except Exception as exc:
        logger.exception(f"[{request_id}] Internal gateway error while proxying {full_path}: {exc}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "error": "Internal Gateway Error",
                "detail": str(exc),
                "request_id": request_id
            },
            headers={"X-Request-ID": request_id}
        )

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("GATEWAY_PORT", 8000))
    uvicorn.run("backend.gateway.main:app", host="0.0.0.0", port=port, reload=True)
