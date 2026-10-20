"""
The user model.
"""

from enum import StrEnum
from typing import Final

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .basemodel import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    fullname: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str]
    role: Mapped[Role]

    class Role(StrEnum):
        ADMIN: Final = "admin"
        EMPLOYEE: Final = "employee"
