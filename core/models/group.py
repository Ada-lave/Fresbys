from sqlalchemy.orm import Mapped, relationship
from .base import Base
from .user import User

class Group(Base):
    name: Mapped[str]
    
    users: Mapped[list["User"]] = relationship(back_populates="group")