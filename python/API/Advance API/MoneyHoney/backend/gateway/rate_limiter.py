import os
import time
import logging
from typing import Tuple, Optional
import redis
from collections import defaultdict, deque

logger = logging.getLogger("moneyhoney.gateway.ratelimit")

class SlidingWindowRateLimiter:
    """
    Production-grade sliding window rate limiter.
    Primary backend: Redis sorted sets (ZADD, ZREMRANGEBYSCORE, ZCARD).
    Fallback backend: In-memory sliding window deque if Redis is unavailable.
    """
    def __init__(self, redis_host: str = "localhost", redis_port: int = 6379, redis_db: int = 0):
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis_db = redis_db
        self.redis_client: Optional[redis.Redis] = None
        self._in_memory_store: dict = defaultdict(deque)

        try:
            self.redis_client = redis.Redis(
                host=self.redis_host,
                port=self.redis_port,
                db=self.redis_db,
                decode_responses=True,
                socket_timeout=0.5,
                socket_connect_timeout=0.5
            )
            self.redis_client.ping()
            logger.info("Connected to Redis for distributed rate limiting.")
        except Exception as exc:
            logger.warning(f"Redis not available for rate limiter ({exc}). Falling back to in-memory rate limiting.")
            self.redis_client = None

    def is_rate_limited(self, identifier: str, limit: int = 60, window_seconds: int = 60) -> Tuple[bool, int, int]:
        """
        Check whether an identifier (IP or User) has exceeded rate limit.
        Returns:
            (is_limited: bool, remaining_requests: int, retry_after_seconds: int)
        """
        current_time = time.time()
        window_start = current_time - window_seconds

        # 1. Try Redis sliding window with sorted set
        if self.redis_client is not None:
            try:
                key = f"ratelimit:{identifier}:{window_seconds}"
                pipe = self.redis_client.pipeline()
                
                # Remove requests older than sliding window
                pipe.zremrangebyscore(key, 0, window_start)
                # Count current requests in window
                pipe.zcard(key)
                # Add current request timestamp as score and member (with microsecond salt)
                pipe.zadd(key, {f"{current_time}_{time.time_ns()}": current_time})
                # Set TTL slightly longer than window
                pipe.expire(key, window_seconds + 5)
                
                results = pipe.execute()
                current_count = results[1]  # count before this request

                if current_count >= limit:
                    # Remove the request that just exceeded limit
                    self.redis_client.zremrangebyrank(key, -1, -1)
                    retry_after = max(1, int(window_seconds - (current_time - window_start)))
                    return True, 0, retry_after

                remaining = max(0, limit - (current_count + 1))
                return False, remaining, 0
            except Exception as exc:
                logger.warning(f"Redis rate check failed ({exc}), falling back to in-memory store.")

        # 2. In-memory sliding window fallback
        queue = self._in_memory_store[identifier]
        while queue and queue[0] <= window_start:
            queue.popleft()

        if len(queue) >= limit:
            oldest_request = queue[0]
            retry_after = max(1, int(window_seconds - (current_time - oldest_request)))
            return True, 0, retry_after

        queue.append(current_time)
        remaining = max(0, limit - len(queue))
        return False, remaining, 0
