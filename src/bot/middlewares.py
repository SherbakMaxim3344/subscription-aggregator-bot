from aiogram import BaseMiddleware
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from src.core.rate_limiter import RateLimiter
from aiogram.types import Message


class DbSessionMiddleware(BaseMiddleware):
    def __init__(self, session_pool: async_sessionmaker[AsyncSession]):
        super().__init__()
        self.session_pool = session_pool

    async def __call__(self, handler, event, data):
        async with self.session_pool() as session:
            data["session"] = session
            return await handler(event, data)


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limiter: RateLimiter, max_requests: int = 3, window_seconds: int = 5):
        self.limiter = limiter
        self.max_requests = max_requests
        self.window_seconds = window_seconds

    async def __call__(self, handler, event: Message, data):
        user = event.from_user
        if user and await self.limiter.is_limited(
            user.id, "bot", self.max_requests, self.window_seconds
        ):
            return 
        return await handler(event, data)
