import os
import sys
import time
import socket
from pathlib import Path
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

# Add project root and backend directory to sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.gurd.auth import router as auth_router
from backend.app.api.v1.endpoints.users import router as users_router
from backend.app.api.v1.endpoints.trades import router as trades_router

# Environment & Worker metadata
WORKER_PORT = os.getenv("PORT", "unknown")
HOSTNAME = socket.gethostname()
WORKER_PID = os.getpid()

app = FastAPI(
    title="MoneyHoney Backend Service",
    description="High-performance financial market data & trading cluster instance",
    version="1.0.0",
    root_path="/mh/v1"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Worker identification and latency tracking middleware
@app.middleware("http")
async def add_worker_metadata(request: Request, call_next):
    start_time = time.perf_counter()
    response: Response = await call_next(request)
    duration_ms = (time.perf_counter() - start_time) * 1000

    # Helpful headers to observe Load Balancer distribution across cluster nodes
    response.headers["X-Worker-PID"] = str(WORKER_PID)
    response.headers["X-Worker-Port"] = str(WORKER_PORT)
    response.headers["X-Worker-Host"] = HOSTNAME
    response.headers["X-Process-Time-Ms"] = f"{duration_ms:.2f}"
    return response

# Cluster instance health check
@app.get("/health", tags=["System"])
def health_check():
    return {
        "status": "healthy",
        "service": "MoneyHoney Backend Node",
        "worker_pid": WORKER_PID,
        "worker_port": WORKER_PORT,
        "hostname": HOSTNAME
    }

# Mount sub-routers
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(trades_router)

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8081))
    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=port, reload=True)
