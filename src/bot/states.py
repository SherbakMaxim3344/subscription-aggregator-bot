from aiogram.fsm.state import State, StatesGroup

class AddSubscription(StatesGroup):
    name = State()          # ввод названия
    price = State()        # ввод суммы
    period = State()        # выбор периода
    next_date = State()  # выбор даты
    confirm = State()       # подтверждение
