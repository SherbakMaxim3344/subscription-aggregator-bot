import pytest
from datetime import date

from src.repositories.subscriptions import add_subscription, delete_subscriptions
from src.models.enums import Period

pytestmark = pytest.mark.integration

async def test_create_subs(session,user):
    sub = await add_subscription(session=session,
                                    user_id=user.tg_id,
                                    name="Max",
                                    price=500,
                                    period=Period.WEEK,
                                    next_payment_date=date(2026, 12, 9)
                                )
    assert sub.user_id == user.tg_id
    assert sub.name == "Max"
    assert sub.price == 500
    assert sub.period == Period.WEEK
    assert sub.next_payment_date == date(2026, 12, 9)


async def test_delete_subs(session, user):
    sub = await add_subscription(session=session,
                                    user_id=user.tg_id,
                                    name="mono",
                                    price=500,
                                    period=Period.WEEK,
                                    next_payment_date=date(2026, 12, 9)
                                )
    deleted = await delete_subscriptions(session=session, subs_id=sub.id, user_id=sub.user_id)
    assert deleted is True
