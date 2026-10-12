"""
MoneyHoney Cluster Orchestrator (Cross-Platform)
Spawns and manages:
  1. Worker 1 on port 8081
  2. Worker 2 on port 8082
  3. Worker 3 on port 8083
  4. Load Balancer on port 8001
  5. API Gateway on port 8000
Press Ctrl+C to terminate the entire cluster cleanly.
"""

import sys
import subprocess
import time
import os
import signal
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PYTHON_EXE = sys.executable

SERVICES = [
    {
        "name": "Auth Microservice (Port 8001)",
        "cmd": [PYTHON_EXE, "-m", "uvicorn", "backend.gurd.auth:app", "--host", "127.0.0.1", "--port", "8001"],
        "env": {"PORT": "8001"}
    },
    {
        "name": "Trades Microservice (Port 8002)",
        "cmd": [PYTHON_EXE, "-m", "uvicorn", "backend.app.api.v1.endpoints.trades:app", "--host", "127.0.0.1", "--port", "8002"],
        "env": {"PORT": "8002"}
    },
    {
        "name": "Market Data Worker #1 (Port 8081)",
        "cmd": [PYTHON_EXE, "-m", "uvicorn", "backend.app.api.v1.endpoints.users:app", "--host", "127.0.0.1", "--port", "8081"],
        "env": {"PORT": "8081"}
    },
    {
        "name": "Market Data Worker #2 (Port 8082)",
        "cmd": [PYTHON_EXE, "-m", "uvicorn", "backend.app.api.v1.endpoints.users:app", "--host", "127.0.0.1", "--port", "8082"],
        "env": {"PORT": "8082"}
    },
    {
        "name": "Market Data Load Balancer (Port 8003)",
        "cmd": [PYTHON_EXE, "-m", "uvicorn", "backend.gateway.load_balancer:app", "--host", "127.0.0.1", "--port", "8003"],
        "env": {"LB_PORT": "8003", "BACKEND_WORKERS": "http://127.0.0.1:8081,http://127.0.0.1:8082"}
    },
    {
        "name": "API Gateway (Port 8000)",
        "cmd": [PYTHON_EXE, "-m", "uvicorn", "backend.gateway.main:app", "--host", "127.0.0.1", "--port", "8000"],
        "env": {
            "GATEWAY_PORT": "8000",
            "AUTH_SERVICE_URL": "http://127.0.0.1:8001",
            "TRADES_SERVICE_URL": "http://127.0.0.1:8002",
            "USERS_SERVICE_URL": "http://127.0.0.1:8003"
        }
    }
]

def main():
    print("=" * 70)
    print("MoneyHoney Microservices Application Cluster")
    print("=" * 70)
    print(f"Working Directory: {PROJECT_ROOT}")
    print(f"Python: {PYTHON_EXE}\n")

    processes = []

    try:
        for s in SERVICES:
            env = os.environ.copy()
            env.update(s["env"])
            env["PYTHONPATH"] = str(PROJECT_ROOT)

            print(f"[*] Starting {s['name']}...")
            proc = subprocess.Popen(
                s["cmd"],
                cwd=str(PROJECT_ROOT),
                env=env,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE
            )
            processes.append((s["name"], proc))
            time.sleep(0.5)

        print("\n" + "=" * 70)
        print("ALL MICROSERVICES ARE UP AND RUNNING!")
        print("   - API Gateway:           http://127.0.0.1:8000 (Central Ingress, Auth & Rate Limiter)")
        print("   - Auth Microservice:     http://127.0.0.1:8001 (/login, /refresh)")
        print("   - Trades Microservice:   http://127.0.0.1:8002 (/trade, /mytrades)")
        print("   - Market Data LB:        http://127.0.0.1:8003 (Load Balancer -> 8081, 8082)")
        print("   - Market Data Worker #1: http://127.0.0.1:8081")
        print("   - Market Data Worker #2: http://127.0.0.1:8082")
        print("=" * 70)
        print("Press Ctrl+C to stop all cluster services...\n")


        while True:
            for name, proc in processes:
                poll = proc.poll()
                if poll is not None:
                    _, err = proc.communicate()
                    err_msg = err.decode(errors="ignore").strip() if err else ""
                    print(f"⚠️ [WARNING] Service '{name}' exited with code {poll}: {err_msg}")
            time.sleep(2)

    except KeyboardInterrupt:
        print("\n[!] Shutting down all cluster processes gracefully...")
        for name, proc in processes:
            print(f"    Stopping {name}...")
            proc.terminate()
            try:
                proc.wait(timeout=3)
            except subprocess.TimeoutExpired:
                proc.kill()
        print("All processes stopped.")

if __name__ == "__main__":
    main()
