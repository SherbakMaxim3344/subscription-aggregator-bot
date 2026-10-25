from aiogram import Router, types, F
from aiogram.filters.command import Command
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.types import Message
from aiogram.types import CallbackQuery

from src.repositories.subscriptions import list_subscriptions, delete_subscription, get_subscription
from src.bot.keybord import PERIOD_LABELS
from src.bot.keybord import delete_confirm_keyboard, delete_list_keyboard


router = Router()

@router.message(Command("subscriptions"))
async def show_subs(message: types.Message, session: AsyncSession):
    subs = await list_subscriptions(session, message.from_user.id)
    if not subs:
        await message.answer("Подписок пока нет. Добавить: /add_subscription")
        return
    lines = [
        f"{s.name}: {s.price} ₽ / {PERIOD_LABELS[s.period]}, "
        f"следующий платёж {s.next_payment_date:%d.%m.%Y}"
        for s in subs
    ]
    await message.answer("Ваши подписки:\n\n" + "\n".join(lines))


@router.message(Command("delete_subscription"))
async def start_delete(message: Message, session: AsyncSession):
    subs = await list_subscriptions(session, message.from_user.id)
    if not subs:
        await message.answer("Подписок пока нет.")
        return
    await message.answer("Какую подписку удалить?", reply_markup=delete_list_keyboard(subs))


@router.callback_query(F.data.startswith("del:"))
async def ask_confirm(cb: CallbackQuery, session: AsyncSession):
    sub_id = int(cb.data.split(":", 1)[1])
    sub = await get_subscription(session, sub_id, cb.from_user.id)
    if sub is None:
        await cb.message.edit_text("Подписка не найдена.")
    else:
        await cb.message.edit_text(f"Удалить «{sub.name}»?", reply_markup=delete_confirm_keyboard(sub_id))
    await cb.answer()


@router.callback_query(F.data.startswith("del_yes:"))
async def do_delete(cb: CallbackQuery, session: AsyncSession):
    sub_id = int(cb.data.split(":", 1)[1])
    ok = await delete_subscription(session, sub_id, cb.from_user.id)
    await cb.message.edit_text("Подписка удалена" if ok else "Подписка уже удалена")
    await cb.answer()


@router.callback_query(F.data == "del_no")
async def cancel_delete(cb: CallbackQuery):
    await cb.message.edit_text("Отменено")
    await cb.answer()


@router.message(Command("delete_all_subscriptions"))
async def delete_subs(message: types.Message, session: AsyncSession):
    pass
