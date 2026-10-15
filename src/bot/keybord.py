from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from src.bot.admins import admins

def main_keyboard(user_tg_id: int):
    kb_list = [
        [KeyboardButton(text='меню')],
        [KeyboardButton(text='помощь')]
    ]
    if user_tg_id in admins:
        kb_list.append([KeyboardButton(text='админ панель')])
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list,resize_keyboard=True,one_time_keyboard=True)
    return keyboard
