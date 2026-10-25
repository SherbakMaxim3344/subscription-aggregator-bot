from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from src.bot.admins import admins
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.models import Period


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



PERIOD_LABELS = {
    Period.WEEK: "Неделя",
    Period.MONTH: "Месяц",
    Period.QUARTER: "3 месяца",
    Period.HALF_YEAR: "6 месяцев",
    Period.YEAR: "Год",
}

def period_keyboard():
    kb = InlineKeyboardBuilder()
    for period, label in PERIOD_LABELS.items():
        kb.button(text=label, callback_data=f"period:{period.value}")
    kb.adjust(2)
    return kb.as_markup()


def confirm_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text="Сохранить", callback_data="confirm:yes")
    kb.button(text="Отмена", callback_data="confirm:no")
    kb.adjust(2)
    return kb.as_markup()


def delete_list_keyboard(subs):
    kb = InlineKeyboardBuilder()
    for s in subs:
        kb.button(text=f" {s.name} — {s.price} ₽", callback_data=f"del:{s.id}")
    kb.adjust(1)
    return kb.as_markup()

def delete_confirm_keyboard(sub_id: int):
    kb = InlineKeyboardBuilder()
    kb.button(text="Да, удалить", callback_data=f"del_yes:{sub_id}")
    kb.button(text="Отмена", callback_data="del_no")
    kb.adjust(2)
    return kb.as_markup()
