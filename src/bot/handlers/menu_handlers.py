from aiogram import Router, types
from aiogram.filters.command import Command

router = Router()

@router.message(Command("menu"))
async def show_menu(message: types.Message):
    text = (
        "<b>Меню:</b>\n\n"
        "<i>Возможности бота:</i>\n"
        " - Высчитывать ваши траты на подписки\n"
        " - Уведомлять когда списание за подписки\n"
    )
    await message.answer(text, parse_mode="HTML")
