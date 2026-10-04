#!/usr/bin/env bash
# ==============================================================================
# MoneyHoney Cluster Startup Script (Linux / Production)
# Launches 3 FastAPI backend instances, native Load Balancer and Gateway
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"

cd "$PROJECT_ROOT"

echo "=================================================="
echo " Starting MoneyHoney Services on Linux Server"
echo "=================================================="

# Export PYTHONPATH
export PYTHONPATH="$PROJECT_ROOT"

# Check virtual environment
if [ -d "$PROJECT_ROOT/.venv" ]; then
    source "$PROJECT_ROOT/.venv/bin/activate"
fi

# 1. Start FastAPI Worker Cluster
echo "[+] Starting Worker #1 on port 8081..."
PORT=8081 uvicorn backend.app.main:app --host 127.0.0.1 --port 8081 --workers 1 > /var/log/moneyhoney-8081.log 2>&1 &

echo "[+] Starting Worker #2 on port 8082..."
PORT=8082 uvicorn backend.app.main:app --host 127.0.0.1 --port 8082 --workers 1 > /var/log/moneyhoney-8082.log 2>&1 &

echo "[+] Starting Worker #3 on port 8083..."
PORT=8083 uvicorn backend.app.main:app --host 127.0.0.1 --port 8083 --workers 1 > /var/log/moneyhoney-8083.log 2>&1 &

# 2. Start API Gateway
echo "[+] Starting API Gateway on port 8000..."
GATEWAY_PORT=8000 UPSTREAM_LB_URL=http://127.0.0.1:8001 uvicorn backend.gateway.main:app --host 127.0.0.1 --port 8000 > /var/log/moneyhoney-gateway.log 2>&1 &

echo "=================================================="
echo " All cluster nodes started in background."
echo " Check /var/log/moneyhoney-*.log for output."
echo "=================================================="
