from datetime import date
from dateutil.relativedelta import relativedelta

from src.models import Period

_PERIOD_DELTA = {
    Period.WEEK: relativedelta(weeks=1),
    Period.MONTH: relativedelta(months=1),
    Period.QUARTER: relativedelta(months=3),
    Period.HALF_YEAR: relativedelta(months=6),
    Period.YEAR: relativedelta(years=1),
}


def add_period(current: date, period: Period) -> date:
    """Прибавляет к дате один период подписки."""
    return current + _PERIOD_DELTA[period]
