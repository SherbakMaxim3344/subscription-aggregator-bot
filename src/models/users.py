from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, createdat


class User(Base):
    __tablename__ = "users"

    tg_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    created_at: Mapped[createdat]
    subscriptions: Mapped[list["Subscription"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

