from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from ..states import AddSubscription
from src.bot.handlers.menu_handlers import show_menu

router = Router()

async def start_add_flow(message: types.Message, state: FSMContext):
    await state.set_state(AddSubscription.name)
    await state.update_data(new_sub={})
    await message.answer("Как называется подписка?")

@router.message(Command("add_subscription"))
async def cmd_add_subscription(message: types.Message, state: FSMContext):
    await start_add_flow(message, state)

@router.callback_query(F.data == "add_sub")
async def cb_add_subscription(cb: types.CallbackQuery, state: FSMContext):
    await start_add_flow(cb.message, state)
    await cb.answer()
