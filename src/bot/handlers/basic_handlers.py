from aiogram import Router, types, F
from aiogram.filters.command import Command

router = Router()

@router.message(F.photo)
async def handler_photo(message: types.Message):
    await message.delete()
    await message.answer("получено фото")

@router.message(F.sticker)
async def handler_sticker(message: types.Message):
    await message.delete()
    await message.answer("получен стикер")

@router.message(F.text)
async def handler_text(message: types.Message):
    await message.delete()
    await message.answer(f"сообщение получено: {message.text}")
