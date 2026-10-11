from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router,types
from aiogram.filters.command import Command
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.users import get_or_create_user

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message, session: AsyncSession):
    await get_or_create_user(session, message.from_user.id)
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="/menu"), KeyboardButton(text="/help")],
        ],
        resize_keyboard=True
    )
    await message.delete()
    await message.answer("Выбери действие:", reply_markup=kb)
