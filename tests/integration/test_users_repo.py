import pytest

from src.repositories.users import get_or_create_user

pytestmark = pytest.mark.integration


async def test_get_or_create_user_creates_new_user(session):
    user = await get_or_create_user(session, tg_id=111)

    assert user.tg_id == 111
    assert user.premium_until is None
