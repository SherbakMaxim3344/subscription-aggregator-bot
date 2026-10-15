from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router,types
from aiogram.filters.command import Command, CommandStart
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.users import get_or_create_user
from src.bot.keybord import main_keyboard

start_router = Router()

@start_router.message(CommandStart())
async def cmd_star(message: types.Message):
    await message.answer("Запуск сообщения по команде /start используя фильтр CommandStart()",
                        reply_markup=main_keyboard(message.from_user.id))
