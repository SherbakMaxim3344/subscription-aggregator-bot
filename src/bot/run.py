import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.storage.redis import RedisStorage


from src.core.config_db import settings
from src.core.database import async_session
from src.bot.bot_settings import set_commands
from src.bot.handlers.keyboard import router as keyboard
from src.bot.handlers.basic_handlers import router as router_basic
from src.bot.handlers.menu_handlers import router as router_menu
from src.bot.handlers.subscriptions import router as router_subscriptions
from src.bot.middlewares import DbSessionMiddleware
from src.bot.handlers.start import start_router as router_start



async def main():
    logging.basicConfig(level=logging.INFO)
    storage = RedisStorage.from_url(settings.REDIS_URL)
    bot = Bot(token=settings.TOKEN_BOT, session=AiohttpSession(proxy=settings.PROXY_URL))
    dp = Dispatcher(storage=storage)
    dp.update.middleware(DbSessionMiddleware(async_session))

    dp.include_router(router_start)
    dp.include_router(keyboard)
    dp.include_router(router_menu)
    dp.include_router(router_subscriptions)
    dp.include_router(router_basic)


    await bot.delete_webhook(drop_pending_updates=True)
    await set_commands(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
