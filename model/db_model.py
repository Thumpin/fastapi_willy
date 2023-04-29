from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    backref,
)
from sqlalchemy import (
    Integer,
    String,
    DECIMAL,
    Boolean,
    DateTime,
    JSON
)
from typing_extensions import Annotated
from sqlalchemy.schema import ForeignKey
from typing import List
import datetime as dt


intpk = Annotated[int, mapped_column(Integer(),primary_key=True, autoincrement=True)]
desc = Annotated[str, mapped_column(String(255), nullable=False)]
comment = Annotated[str, mapped_column(String(1000), nullable=False)]
desc_unique = Annotated[str, mapped_column(String(255), nullable=False, unique=False)]
decimal_20_3 = Annotated[float, mapped_column(DECIMAL(precision=20, scale=10, asdecimal=True), nullable=True)]
code = Annotated[int, mapped_column(Integer(), unique=True, nullable=True)]
user = Annotated[str, mapped_column(String(70))]
intnull = Annotated[int, mapped_column(Integer(), nullable=True)]
units = Annotated[str, mapped_column(String(20), unique=True)]
names = Annotated[str, mapped_column(String(255), nullable=True)]
boolean = Annotated[bool, mapped_column(Boolean(), default=False)]
datetime = Annotated[dt.datetime, mapped_column(DateTime(), default=dt.datetime.now())]
on_update = Annotated[dt.datetime, mapped_column(DateTime(), default=dt.datetime.now(), onupdate=dt.datetime.now())]
jsonsql = Annotated[dict, mapped_column(JSON, nullable=True)]

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    username : Mapped[desc]
    password: Mapped[comment]
    name: Mapped[desc]
    department_id = mapped_column(ForeignKey("departments.id"))

    department : Mapped["Department"] = relationship(back_populates="users")

class Department(Base):
    __tablename__ = "departments"

    id: Mapped[intpk]
    name: Mapped[desc]

    users : Mapped[List["User"]] = relationship(back_populates="department")