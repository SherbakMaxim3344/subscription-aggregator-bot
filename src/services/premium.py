from datetime import date

from src.models import Period
from .periods import add_period


def is_premium_active(premium_until: date | None, today: date) -> bool:
    return premium_until is not None and premium_until >= today


def extend_premium(premium_until: date | None, period: Period, today: date) -> date:
    """Новая дата окончания премиума после покупки.
    Если премиум ещё активен, отсчёт идёт от его конца, чтобы оплаченные дни не пропали."""
    start = premium_until if is_premium_active(premium_until, today) else today
    return add_period(start, period)
