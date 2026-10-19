from aiogram import Router, types
from aiogram.filters.command import Command
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.subscriptions import list_subscriptions
from src.bot.keybord import PERIOD_LABELS

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
