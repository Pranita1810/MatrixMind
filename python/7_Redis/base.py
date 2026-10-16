"""Let's Build a simple redis server & client."""
import redis

# ----- REDIS SERVER -----
redis_server = redis.Redis(
                            host='localhost',
                            port = 6379,
                            decode_responses=True
                            )
"""Above is redis server """

