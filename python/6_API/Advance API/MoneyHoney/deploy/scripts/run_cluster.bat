@echo off
title MoneyHoney Cluster Runner
echo ===================================================
echo  Starting MoneyHoney Full Cluster (Workers + LB + Gateway)
echo ===================================================

cd /d "%~dp0..\.."

if exist .venv\Scripts\python.exe (
    set "PYTHON_CMD=.venv\Scripts\python.exe"
) else (
    set "PYTHON_CMD=python"
)

"%PYTHON_CMD%" deploy\scripts\run_cluster.py

pause
