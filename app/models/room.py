from typing import TYPE_CHECKING

import uuid
from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .room import Room  # noqa: F401


class Room(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    joincode = Column(String, index=True)
    users = relationship("User", back_populates="room")
