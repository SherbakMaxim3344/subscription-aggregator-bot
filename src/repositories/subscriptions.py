from  src.models import Subscription

async def add_subscription(session, user_id, name, price, period, next_payment_date):
    sub = Subscription(
        user_id=user_id, name=name, price=price,
        period=period, next_payment_date=next_payment_date,
    )
    session.add(sub)
    await session.commit()
    return sub
