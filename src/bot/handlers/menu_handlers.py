from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.message(Command("menu"))
async def show_menu(message: types.Message):
    text = (
        "<b>Меню:</b>\n\n"
        "<i>Возможности бота:</i>\n"
        " - Высчитывать ваши траты на подписки\n"
        " - Уведомлять когда списание за подписки\n"
    )
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Добавить подписку", callback_data="add_sub")],
            [InlineKeyboardButton(text="Мои подписки", callback_data="my_subs")],
        ]
    )
    await message.delete()
    await message.answer(text, parse_mode="HTML", reply_markup=kb)
