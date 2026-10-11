from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from ..states import AddSubscription
from src.bot.handlers.menu_handlers import show_menu

router = Router()

@router.message(Command("add_subscription"))
@router.callback_query(F.data == "add_sub")
async def add_subscription(message: types.Message, state: FSMContext):
    await state.set_state(AddSubscription.name)
    await state.update_data(new_sub={})
    await message.answer("Как называется подписка?\n\n/cancel - отменить")

@router.message(Command("cancel"))
async def cancel(message: types.Message, state: FSMContext):
    if await state.get_state() is None:
        return
    await state.clear()
    await message.answer("Отменено")
    await show_menu(message)

@router.callback_query(F.data == "my_subs")
async def cb_my_subs(cb: types.CallbackQuery):
    await cb.message.answer("Тут список подписок")
    await cb.answer()
