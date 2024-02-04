from typing import Optional
from pydantic import BaseModel
from uuid import UUID

# Shared properties
class PlaceBase(BaseModel):
    name: Optional[str] = None
    joincode: Optional[str] = None

# Properties to receive via API on creation
class PlaceCreate(PlaceBase):
    name: str
    joincode: str

# Properties to receive via API on update
class PlaceUpdate(PlaceBase):
    pass

class PlaceInDBBase(PlaceBase):
    id: UUID
    name: str
    joincode: str

# Additional properties to return via API
class Place(PlaceInDBBase):
    pass

# Additional properties stored in DB
class PlaceInDB(PlaceInDBBase):
    pass