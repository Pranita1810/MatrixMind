#!/usr/bin/env bash
# ==============================================================================
# AutoSSH Tunnel Script
# Bridges Linux Server to Windows Laptop SSMS SQL Server on Port 1433
# ==============================================================================

set -e

LAPTOP_USER="${LAPTOP_USER:-panrit}"
LAPTOP_HOST="${LAPTOP_HOST:-192.168.1.100}"
REMOTE_PORT=1433
LOCAL_PORT=1433

echo "Starting SSH Tunnel forwarding local port $LOCAL_PORT to $LAPTOP_HOST:$REMOTE_PORT..."

autossh -M 0 -o "ServerAliveInterval 30" -o "ServerAliveCountMax 3" -o "ExitOnForwardFailure yes" \
    -N -L 127.0.0.1:${LOCAL_PORT}:127.0.0.1:${REMOTE_PORT} ${LAPTOP_USER}@${LAPTOP_HOST}
