import os
import sys
import asyncio
import time
import logging
from pathlib import Path
from typing import List, Dict, Any

import httpx
from fastapi import FastAPI, Request, Response, status
from fastapi.responses import JSONResponse, StreamingResponse
from dotenv import load_dotenv

load_dotenv()

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] [LB] %(message)s")
logger = logging.getLogger("moneyhoney.loadbalancer")

# Configure backend worker pool from environment or defaults
DEFAULT_WORKERS = ["http://127.0.0.1:8081", "http://127.0.0.1:8082", "http://127.0.0.1:8083"]
WORKER_URLS_ENV = os.getenv("BACKEND_WORKERS")
WORKER_URLS = [w.strip() for w in WORKER_URLS_ENV.split(",")] if WORKER_URLS_ENV else DEFAULT_WORKERS

LB_PORT = int(os.getenv("LB_PORT", 8003))
LB_ALGORITHM = os.getenv("LB_ALGORITHM", "round_robin")  # round_robin or least_conn


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

class BackendNode:
    def __init__(self, url: str):
        self.url = url.rstrip("/")
        self.is_healthy = True
        self.active_connections = 0
        self.total_requests = 0
        self.failed_checks = 0

    def __repr__(self):
        return f"<BackendNode url={self.url} healthy={self.is_healthy} active={self.active_connections} total={self.total_requests}>"

class LoadBalancer:
    def __init__(self, workers: List[str]):
        self.nodes = [BackendNode(url) for url in workers]
        self._rr_index = 0
        self._lock = asyncio.Lock()

    def get_healthy_nodes(self) -> List[BackendNode]:
        return [node for node in self.nodes if node.is_healthy]

    async def select_node(self) -> BackendNode:
        healthy = self.get_healthy_nodes()
        if not healthy:
            # If all health checks failed, try all nodes as last resort
            healthy = self.nodes

        if LB_ALGORITHM == "least_conn":
            # Pick node with lowest active connections
            return min(healthy, key=lambda n: n.active_connections)
        else:
            # Default: Round Robin
            async with self._lock:
                self._rr_index = (self._rr_index + 1) % len(healthy)
                return healthy[self._rr_index]

app = FastAPI(
    title="MoneyHoney Load Balancer",
    description="High-performance async load balancer distributing traffic across FastAPI backend instances",
    version="1.0.0"
)

lb = LoadBalancer(WORKER_URLS)
http_client: httpx.AsyncClient = None
health_task: asyncio.Task = None

async def health_check_loop():
    """Periodic background health checker for backend worker nodes."""
    client = httpx.AsyncClient(timeout=2.0)
    while True:
        try:
            for node in lb.nodes:
                try:
                    resp = await client.get(f"{node.url}/mh/v1/health")
                    if resp.status_code == 200:
                        if not node.is_healthy:
                            logger.info(f"Node {node.url} recovered and marked HEALTHY.")
                        node.is_healthy = True
                        node.failed_checks = 0
                    else:
                        node.failed_checks += 1
                        if node.failed_checks >= 2 and node.is_healthy:
                            logger.warning(f"Node {node.url} returned status {resp.status_code}. Marking UNHEALTHY.")
                            node.is_healthy = False
                except Exception:
                    node.failed_checks += 1
                    if node.failed_checks >= 2 and node.is_healthy:
                        logger.warning(f"Node {node.url} unreachable. Marking UNHEALTHY.")
                        node.is_healthy = False
        except Exception as exc:
            logger.error(f"Error during health check cycle: {exc}")
        await asyncio.sleep(5)

def get_http_client() -> httpx.AsyncClient:
    global http_client
    if http_client is None or http_client.is_closed:
        http_client = httpx.AsyncClient(
            timeout=httpx.Timeout(connect=5.0, read=30.0, write=10.0, pool=30.0),
            limits=httpx.Limits(max_keepalive_connections=150, max_connections=300)
        )
    return http_client

@app.on_event("startup")
async def startup():
    global health_task
    get_http_client()
    health_task = asyncio.create_task(health_check_loop())
    logger.info(f"Load Balancer active on port {LB_PORT}. Workers: {[n.url for n in lb.nodes]}")

@app.on_event("shutdown")
async def shutdown():
    global http_client, health_task
    if health_task:
        health_task.cancel()
    if http_client and not http_client.is_closed:
        await http_client.aclose()
        logger.info("Load Balancer client closed.")

@app.get("/health", tags=["Load Balancer Diagnostics"])
@app.get("/lb-status", tags=["Load Balancer Diagnostics"])
def lb_status():
    """Status endpoint reporting live backend pool health and metrics."""
    return {
        "status": "healthy",
        "algorithm": LB_ALGORITHM,
        "workers": [
            {
                "url": node.url,
                "healthy": node.is_healthy,
                "active_connections": node.active_connections,
                "total_requests": node.total_requests,
                "failed_checks": node.failed_checks
            }
            for node in lb.nodes
        ]
    }

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"])
async def route_request(request: Request, path: str):
    """Distribute incoming request to a healthy worker node."""
    node = await lb.select_node()
    node.active_connections += 1
    node.total_requests += 1

    target_url = f"{node.url}/{path}"
    if request.url.query:
        target_url = f"{target_url}?{request.url.query}"

    forward_headers = {
        k: v for k, v in request.headers.items()
        if k.lower() not in HOP_BY_HOP_HEADERS and k.lower() != "host"
    }

    body = await request.body()
    start_time = time.perf_counter()

    try:
        client = get_http_client()
        upstream_req = client.build_request(
            method=request.method,
            url=target_url,
            headers=forward_headers,
            content=body
        )
        upstream_resp = await client.send(upstream_req, stream=True)


        resp_headers = {
            k: v for k, v in upstream_resp.headers.items()
            if k.lower() not in HOP_BY_HOP_HEADERS
        }
        resp_headers["X-Load-Balancer"] = "MoneyHoney-LB-8001"
        resp_headers["X-Routed-Worker"] = node.url
        resp_headers["X-LB-Latency-Ms"] = f"{(time.perf_counter() - start_time) * 1000:.2f}"

        async def stream_and_cleanup():
            try:
                async for chunk in upstream_resp.aiter_raw():
                    yield chunk
            finally:
                node.active_connections = max(0, node.active_connections - 1)
                await upstream_resp.aclose()

        return StreamingResponse(
            stream_and_cleanup(),
            status_code=upstream_resp.status_code,
            headers=resp_headers
        )

    except Exception as exc:
        node.active_connections = max(0, node.active_connections - 1)
        logger.error(f"Error forwarding request to worker {node.url}: {exc}")
        return JSONResponse(
            status_code=status.HTTP_502_BAD_GATEWAY,
            content={
                "error": "Bad Gateway",
                "detail": f"Worker {node.url} failed to respond.",
                "message": str(exc)
            },
            headers={"X-Routed-Worker": node.url}
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.gateway.load_balancer:app", host="0.0.0.0", port=LB_PORT, reload=True)
