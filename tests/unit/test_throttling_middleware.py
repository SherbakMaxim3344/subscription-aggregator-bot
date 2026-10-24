from types import SimpleNamespace
from src.bot.middlewares import ThrottlingMiddleware


class FakeLimiter:
    def __init__(self, limited: bool):
        self.limited = limited

    async def is_limited(self, *args, **kwargs) -> bool:
        return self.limited


async def test_blocks_when_limited():
    called = False

    async def handler(event, data):
        nonlocal called
        called = True

    mw = ThrottlingMiddleware(FakeLimiter(limited=True))
    event = SimpleNamespace(from_user=SimpleNamespace(id=1))
    await mw(handler, event, {})
    assert called is False
