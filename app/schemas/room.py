from typing import Optional
from pydantic import BaseModel
from uuid import UUID

# Shared properties
class RoomBase(BaseModel):
    name: Optional[str] = None
    joincode: Optional[str] = None

# Properties to receive via API on creation
class RoomCreate(RoomBase):
    name: str
    joincode: str

# Properties to receive via API on update
class RoomUpdate(RoomBase):
    pass

class RoomInDBBase(RoomBase):
    id: UUID
    name: str
    joincode: str

# Additional properties to return via API
class Room(RoomInDBBase):
    pass

# Additional properties stored in DB
class RoomInDB(RoomInDBBase):
    pass