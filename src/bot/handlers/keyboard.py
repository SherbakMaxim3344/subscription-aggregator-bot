from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router,types
from aiogram.filters.command import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="/menu"), KeyboardButton(text="/help")],
        ],
        resize_keyboard=True
    )
    await message.answer("Выбери действие:", reply_markup=kb)
