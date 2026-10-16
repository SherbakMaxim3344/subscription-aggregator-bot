from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from src.bot.admins import admins

def main_keyboard(user_tg_id: int):
    kb_list = [
        [KeyboardButton(text='меню'), KeyboardButton(text='помощь')],
    ]
    if user_tg_id in admins:
        kb_list.append([KeyboardButton(text='админ панель')])
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True, #авто изменяет размер
        one_time_keyboard=True, #скрывать после 1 использования
        input_field_placeholder="Воспользуйтесь меню:", #заменяет стандартную подпись, в сообщении у user отображаться будет эта подпись
    )
    return keyboard
