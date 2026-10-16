from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def link_kb():
    inline_kb_list=[
        [InlineKeyboardButton(text="Мой хабр", url="https://habr.com/ru/users/Kaiser_DW/")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)
