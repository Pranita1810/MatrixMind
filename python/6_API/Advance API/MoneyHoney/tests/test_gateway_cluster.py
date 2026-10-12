"""
Comprehensive Test Suite for MoneyHoney API Gateway, Rate Limiting, and Load Balancer
"""

import sys
import time
from pathlib import Path
from starlette.testclient import TestClient

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.gateway.rate_limiter import SlidingWindowRateLimiter
from backend.app.main import app as backend_app
from backend.gateway.main import app as gateway_app
from backend.gateway.load_balancer import LoadBalancer

def test_sliding_window_rate_limiter():
    print("\n[TEST 1] Testing Sliding Window Rate Limiter...")
    limiter = SlidingWindowRateLimiter()
    test_id = f"test_client_{time.time()}"
    limit = 5
    window = 2

    # First 5 requests should pass
    for i in range(limit):
        is_limited, remaining, retry = limiter.is_rate_limited(test_id, limit=limit, window_seconds=window)
        assert not is_limited, f"Request {i+1} should not be limited"
        print(f"  Request {i+1}: Allowed, Remaining={remaining}")

    # 6th request should be blocked (HTTP 429 condition)
    is_limited, remaining, retry = limiter.is_rate_limited(test_id, limit=limit, window_seconds=window)
    assert is_limited, "Request 6 should be blocked by rate limiter"
    assert retry > 0, "Retry after should be positive"
    print(f"  Request 6: BLOCKED as expected! (Retry after: {retry}s)")

    # Wait for window to expire
    print(f"  Waiting {window + 0.5}s for rate limit window to reset...")
    time.sleep(window + 0.5)

    is_limited, remaining, retry = limiter.is_rate_limited(test_id, limit=limit, window_seconds=window)
    assert not is_limited, "Request after window reset should be allowed"
    print("  Request after reset: Allowed! Rate limiter reset verified.")
    print("  --> PASS: Sliding Window Rate Limiter")


def test_backend_app():
    print("\n[TEST 2] Testing Backend Cluster App Entrypoint...")
    client = TestClient(backend_app)
    resp = client.get("/health")
    assert resp.status_code == 200, f"Health check failed: {resp.text}"
    data = resp.json()
    assert data["status"] == "healthy"
    print(f"  Backend Health Check: OK (Worker PID: {data.get('worker_pid')})")

    # Check response headers injected by backend worker middleware
    assert "X-Worker-PID" in resp.headers
    assert "X-Process-Time-Ms" in resp.headers
    print(f"  Backend Headers: X-Worker-PID={resp.headers['X-Worker-PID']}, Latency={resp.headers['X-Process-Time-Ms']}ms")
    print("  --> PASS: Backend Cluster Application")


def test_gateway_security_and_ratelimit():
    print("\n[TEST 3] Testing API Gateway Security & Rate Limiting Enforcement...")
    client = TestClient(gateway_app)

    # 1. Gateway Health
    resp = client.get("/health")
    assert resp.status_code == 200
    print(f"  Gateway Health: {resp.json().get('gateway_status')}")

    # 2. Protected Route without Token should return 401
    resp = client.get("/mh/v1/watchlist/1")
    assert resp.status_code == 401, f"Expected 401 Unauthorized, got {resp.status_code}"
    assert "X-Request-ID" in resp.headers
    print(f"  Unauthorized Route Blocked at Gateway: HTTP 401 (X-Request-ID: {resp.headers['X-Request-ID']})")

    # 3. Trigger Gateway Rate Limiter on login
    print("  Sending burst of requests to /mh/v1/login to test rate limiting...")
    rate_limited_hit = False
    for i in range(15):
        resp = client.post("/mh/v1/login", headers={"Authorization": "Basic dGVzdDp0ZXN0"})
        if resp.status_code == 429:
            rate_limited_hit = True
            assert "Retry-After" in resp.headers
            assert "X-RateLimit-Limit" in resp.headers
            print(f"  Rate Limit Triggered at attempt {i+1}: HTTP 429 Too Many Requests (Retry-After: {resp.headers['Retry-After']}s)")
            break

    assert rate_limited_hit, "Expected 429 Too Many Requests to be triggered"
    print("  --> PASS: API Gateway Security & Rate Limiting")


def test_microservice_resolution():
    print("\n[TEST 4] Testing Gateway Path-Based Microservice Resolution...")
    from backend.gateway.main import resolve_microservice, AUTH_SERVICE_URL, TRADES_SERVICE_URL, USERS_SERVICE_URL

    # Auth routes
    url, name = resolve_microservice("/mh/v1/login")
    assert name == "Auth Microservice" and url == AUTH_SERVICE_URL
    url, name = resolve_microservice("/refresh")
    assert name == "Auth Microservice" and url == AUTH_SERVICE_URL
    print(f"  /login & /refresh resolved to -> {name} ({url})")

    # Trades routes
    url, name = resolve_microservice("/mh/v1/trade")
    assert name == "Trades Microservice" and url == TRADES_SERVICE_URL
    url, name = resolve_microservice("/mytrades/1")
    assert name == "Trades Microservice" and url == TRADES_SERVICE_URL
    print(f"  /trade & /mytrades resolved to -> {name} ({url})")

    # Users & Market Data routes
    url, name = resolve_microservice("/mh/v1/get_data/RELIANCE")
    assert name == "Users/Market Data Microservice" and url == USERS_SERVICE_URL
    url, name = resolve_microservice("/watchlist/10")
    assert name == "Users/Market Data Microservice" and url == USERS_SERVICE_URL
    print(f"  /get_data & /watchlist resolved to -> {name} ({url})")
    print("  --> PASS: Gateway Path-Based Microservice Resolution")



def test_load_balancer_logic():
    print("\n[TEST 4] Testing Load Balancer Distribution Logic...")
    workers = ["http://127.0.0.1:8081", "http://127.0.0.1:8082", "http://127.0.0.1:8083"]
    lb = LoadBalancer(workers)

    import asyncio
    async def run_lb_test():
        chosen_nodes = []
        for _ in range(6):
            node = await lb.select_node()
            chosen_nodes.append(node.url)
        return chosen_nodes

    selected = asyncio.run(run_lb_test())
    print(f"  6 consecutive node selections: {selected}")
    # Verify Round-Robin rotation
    assert selected == [
        "http://127.0.0.1:8082",
        "http://127.0.0.1:8083",
        "http://127.0.0.1:8081",
        "http://127.0.0.1:8082",
        "http://127.0.0.1:8083",
        "http://127.0.0.1:8081"
    ], f"Unexpected rotation pattern: {selected}"
    print("  Round-Robin distribution across all 3 nodes verified!")
    print("  --> PASS: Load Balancer Selection Logic")


if __name__ == "__main__":
    print("=" * 70)
    print("Running MoneyHoney Gateway, Rate Limiting & Load Balancer Test Suite")
    print("=" * 70)
    test_sliding_window_rate_limiter()
    test_backend_app()
    test_gateway_security_and_ratelimit()
    test_microservice_resolution()
    test_load_balancer_logic()
    print("\n" + "=" * 70)
    print("[SUCCESS] ALL TESTS PASSED SUCCESSFULLY!")
    print("=" * 70)



