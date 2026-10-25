from datetime import date
from decimal import Decimal

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Subscription, Period


async def add_subscription(session, user_id, name, price, period, next_payment_date):
    sub = Subscription(
        user_id=user_id, name=name, price=price,
        period=period, next_payment_date=next_payment_date,
    )
    session.add(sub)
    await session.commit()
    return sub

async def list_subscriptions(session: AsyncSession, user_id: int):
    res = await session.execute(
        select(Subscription)
        .where(Subscription.user_id==user_id)
        .order_by(Subscription.next_payment_date)
    )
    return list(res.scalars().all())

async def delete_subscription(session: AsyncSession, subs_id: int, user_id: int):
    res = await session.execute(
        delete(Subscription)
        .where(Subscription.id == subs_id, Subscription.user_id == user_id)
    )
    await session.commit()
    return res.rowcount > 0


async def get_subscription(session: AsyncSession, sub_id: int, user_id: int) -> Subscription | None:
    result = await session.execute(
        select(Subscription).where(Subscription.id == sub_id, Subscription.user_id == user_id)
    )
    return result.scalar_one_or_none()
