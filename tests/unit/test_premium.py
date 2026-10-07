from datetime import date

from src.models import Period
from src.services.premium import extend_premium, is_premium_active

TODAY = date(2026, 10, 7)


def test_no_premium():
    assert is_premium_active(None, TODAY) is False

def test_premium_until_today_is_active():
    assert is_premium_active(TODAY, TODAY) is True

def test_premium_expired():
    assert is_premium_active(date(2026, 10, 6), TODAY) is False

def test_extend_from_scratch():
    assert extend_premium(None, Period.MONTH, TODAY) == date(2026, 11, 7)

def test_extend_active_keeps_remaining_days():
    assert extend_premium(date(2026, 10, 20), Period.MONTH, TODAY) == date(2026, 11, 20)

def test_extend_expired_starts_from_today():
    assert extend_premium(date(2026, 9, 1), Period.QUARTER, TODAY) == date(2027, 1, 7)
