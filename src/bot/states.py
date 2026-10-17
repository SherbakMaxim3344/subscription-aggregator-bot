from asyncio import sleep
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender
from aiogram import Bot
from aiogram.types import CallbackQuery
from datetime import datetime, date
from decimal import Decimal
from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.keybord import period_keyboard, confirm_keyboard, PERIOD_LABELS, Period
from src.repositories.users import get_or_create_user
from src.repositories.subscriptions import add_subscription


class AddSubscription(StatesGroup):
    name = State()          # ввод названия
    price = State()        # ввод суммы
    period = State()        # выбор периода
    next_date = State()  # выбор даты
    confirm = State()       # подтверждение

time_sleep=1

router = Router()

@router.message(Command("add_subscription"))
async def start_add_sub(message: Message, state: FSMContext, bot: Bot):
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        await sleep(time_sleep)
        await message.answer("Напишите название подписки. Формат: Spotify")
    await message.delete()
    await state.set_state(AddSubscription.name)


@router.message(F.text, AddSubscription.name)
async def capture_name(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(name=message.text)
    async with ChatActionSender(bot=bot, chat_id=message.chat.id):
        await sleep(time_sleep)
        await message.answer("Напишите стоимость подписки. Формат: 500 или 499.90")
    await state.set_state(AddSubscription.price)


@router.message(F.text, AddSubscription.price)
async def capture_price(message: Message, state: FSMContext, bot: Bot):
    try:
        price = Decimal(message.text.strip().replace(",", "."))
        if price <= 0:
            raise ValueError
    except Exception:
        await message.answer("Не понял сумму. Формат: 500 или 499.90")
        return
    await state.update_data(price=str(price))
    async with ChatActionSender(bot=bot, chat_id=message.chat.id):
        await sleep(time_sleep)
        await message.answer("Выберите период оплаты:", reply_markup=period_keyboard())
    await state.set_state(AddSubscription.period)


@router.callback_query(F.data.startswith("period:"), AddSubscription.period)
async def capture_period(cb: CallbackQuery, state: FSMContext):
    period = Period(cb.data.split(":", 1)[1])
    await state.update_data(period=period.value)
    await cb.message.edit_text("Когда следующий платёж? Формат: 25.10.2026")
    await state.set_state(AddSubscription.next_date)
    await cb.answer()


@router.message(F.text, AddSubscription.next_date)
async def capture_data(message: Message, state: FSMContext, bot: Bot):
    try:
        d = datetime.strptime(message.text.strip(), "%d.%m.%Y").date()
    except ValueError:
        await message.answer("Не понял дату. Формат: 25.10.2026")
        return
    if d < date.today():
        await message.answer("Дата уже прошла. Введите ближайшее будущее списание.")
        return
    await state.update_data(next_date=d.isoformat())
    data = await state.get_data()
    text = (
        "Все поля заполнены, проверьте их:\n\n"
        f"Название: {data['name']}\n"
        f"Цена: {data['price']} ₽\n"
        f"Период: {PERIOD_LABELS[Period(data['period'])]}\n"
        f"Следующий платёж: {d.strftime('%d.%m.%Y')}"
    )
    async with ChatActionSender(bot=bot, chat_id=message.chat.id):
        await sleep(time_sleep)
        await message.answer(text, reply_markup=confirm_keyboard())
    await state.set_state(AddSubscription.confirm)


@router.callback_query(F.data == "confirm:yes", AddSubscription.confirm)
async def confirm(cb: CallbackQuery, state: FSMContext, session: AsyncSession):
    data = await state.get_data()
    await get_or_create_user(session, cb.from_user.id)
    await add_subscription(
        session,
        user_id=cb.from_user.id,
        name=data["name"],
        price=Decimal(data["price"]),
        period=Period(data["period"]),
        next_payment_date=date.fromisoformat(data["next_date"]),
    )
    await state.clear()
    await cb.message.edit_text("Подписка сохранена")
    await cb.answer()


@router.callback_query(F.data == "confirm:no", AddSubscription.confirm)
async def confirm_cancel(cb: CallbackQuery, state: FSMContext):
    await state.clear()
    await cb.message.edit_text("Отменено. Начать заново: /add_sub")
    await cb.answer()
