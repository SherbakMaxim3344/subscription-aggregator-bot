import pytest

from src.repositories.users import get_all_users, get_or_create_user

pytestmark = pytest.mark.integration


async def test_get_or_create_user_creates_new_user(session):
    user = await get_or_create_user(session, tg_id=111)

    assert user.tg_id == 111
    assert user.premium_until is None

async def test_get_all_users(session):
    user1 = await get_or_create_user(session, tg_id=111)
    user2 = await get_or_create_user(session, tg_id=222)

    users = await get_all_users(session)

    assert len(users) == 2
    assert users[0].tg_id == 111
    assert users[1].tg_id == 222
