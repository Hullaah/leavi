"""
Base model for all database tables.
"""

from datetime import UTC, datetime
from uuid import UUID, uuid4

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """
    Base class for all database tables.
    """


class BaseModel(Base):
    """
    Base model for all database tables
    """

    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )
    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
