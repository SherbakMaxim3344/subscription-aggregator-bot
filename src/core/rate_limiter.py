import uuid
from time import time

from redis.asyncio import Redis


class RateLimiter:
    def __init__(self, redis: Redis):
        self._redis = redis

    async def is_limited(
        self, user_id: int, category: str, max_requests: int, window_seconds: int
    ) -> bool:
        key = f"rate_limiter:{category}:{user_id}"
        now_ms = time() * 1000
        window_start_ms = now_ms - window_seconds * 1000
        member = f"{now_ms}-{uuid.uuid4().hex[:8]}"

        async with self._redis.pipeline() as pipe:
            pipe.zremrangebyscore(key, 0, window_start_ms)
            pipe.zcard(key)
            pipe.zadd(key, {member: now_ms})
            pipe.expire(key, window_seconds)
            _, current_count, _, _ = await pipe.execute()

        return current_count >= max_requests
