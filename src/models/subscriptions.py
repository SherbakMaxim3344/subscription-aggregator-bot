import datetime
from decimal import Decimal

from sqlalchemy import BigInteger, Date, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, intpk, str_256, createdat
from .enums import Period

class Subscription(Base):
    __tablename__ = "subscriptions"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.tg_id", ondelete="CASCADE"), index=True
    )
    name: Mapped[str_256]
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    period: Mapped[Period]

    next_payment_date: Mapped[datetime.date] = mapped_column(Date)
    created_at: Mapped[createdat]

    user: Mapped["User"] = relationship(back_populates="subscriptions")
