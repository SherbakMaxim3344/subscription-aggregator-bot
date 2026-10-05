from typing import Annotated
from sqlalchemy import text, MetaData, String
from sqlalchemy.orm import mapped_column, DeclarativeBase
import datetime


intpk = Annotated[int, mapped_column(primary_key=True)]

str_256 = Annotated[str, 256]

createdat = Annotated[
    datetime.datetime,
    mapped_column(server_default=text("TIMEZONE('utc', now())"))
]

updatedat = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=text("TIMEZONE('utc', now())"),
    ),
]

datat = Annotated[datetime.date, mapped_column(server_default=text("CURRENT_DATE"))]

class Base(DeclarativeBase):
    metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    })
    type_annotation_map = {str_256: String(256)}
