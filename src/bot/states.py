from aiogram.fsm.state import State, StatesGroup

class AddSubscription(StatesGroup):
    name = State()          # ввод названия (текст)
    amount = State()        # ввод суммы (текст)
    currency = State()      # выбор валюты (кнопки)
    period = State()        # выбор периода (кнопки)
    next_payment = State()  # выбор даты (кнопки)
    confirm = State()       # подтверждение
