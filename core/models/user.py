from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .group import Group

class User(Base):
    first_name: Mapped[str]
    last_name: Mapped[str]
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    
    group: Mapped["Group"] = relationship(back_populates="users")