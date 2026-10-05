from typing_extensions import Annotated
from sqlalchemy import String
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from .config_db import settings

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
)

async_session = async_sessionmaker(async_engine, expire_on_commit=False)
