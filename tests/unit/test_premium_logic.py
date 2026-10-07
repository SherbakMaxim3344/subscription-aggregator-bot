from datetime import date

import pytest

from src.models import Period
from src.services.periods import add_period


@pytest.mark.parametrize(
    "current, expected",
    [
        (date(2026, 10, 10), date(2026, 10, 17)),
        (date(2026, 10, 28), date(2026, 11, 4)),
        (date(2026, 12, 28), date(2027, 1, 4)),
    ],
)
def test_next_payment_date_week(current, expected):
    assert add_period(current, Period.WEEK) == expected


@pytest.mark.parametrize(
    "current, expected",
    [
        (date(2026, 10, 10), date(2026, 11, 10)),
        (date(2026, 12, 15), date(2027, 1, 15)),
        (date(2026, 1, 31), date(2026, 2, 28)),
        (date(2024, 1, 31), date(2024, 2, 29)),
    ],
)
def test_next_payment_date_month(current, expected):
    assert add_period(current, Period.MONTH) == expected


@pytest.mark.parametrize(
    "current, expected",
    [
        (date(2026, 10, 10), date(2027, 10, 10)),
        (date(2024, 2, 29), date(2025, 2, 28)),
    ],
)
def test_next_payment_date_year(current, expected):
    assert add_period(current, Period.YEAR) == expected


@pytest.mark.parametrize("current, expected", [
    (date(2026, 10, 10), date(2027, 1, 10)),
    (date(2026, 11, 30), date(2027, 2, 28)),
])
def test_add_period_quarter(current, expected):
    assert add_period(current, Period.QUARTER) == expected


@pytest.mark.parametrize("current, expected", [
    (date(2026, 10, 10), date(2027, 4, 10)),
    (date(2026, 8, 31), date(2027, 2, 28)),
])
def test_add_period_half_year(current, expected):
    assert add_period(current, Period.HALF_YEAR) == expected
