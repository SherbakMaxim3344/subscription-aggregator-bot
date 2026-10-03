import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from aiogram.client.session.aiohttp import AiohttpSession

from bot_settings import set_commands
from handlers.keyboard import router as keyboard
from handlers.basic_handlers import router as router_basic
from handlers.menu_handlers import router as router_menu

load_dotenv()
BOT_TOKEN = os.getenv("TOKEN_BOT")
PROXY_URL = os.getenv("PROXY_URL")

logging.basicConfig(level=logging.INFO)

session = AiohttpSession(proxy=PROXY_URL)
bot = Bot(token=BOT_TOKEN, session=session)
dp=Dispatcher()

async def main():
    dp.include_router(keyboard)
    dp.include_router(router_menu)
    dp.include_router(router_basic)


    await bot.delete_webhook(drop_pending_updates=True)
    await set_commands(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
