from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import User

async def get_or_create_user(session: AsyncSession, tg_id: int) -> User:
    stmt = insert(User).values(tg_id=tg_id).on_conflict_do_nothing(index_elements=["tg_id"])
    await session.execute(stmt)
    await session.commit()
    return await session.get(User, tg_id)


async def get_all_users(session: AsyncSession) -> list[User]:
    stmt = select(User)
    result = await session.execute(stmt)
    return result.scalars().all()
