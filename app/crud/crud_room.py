from typing import List
from uuid import UUID
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.room import Room
from app.schemas.room import RoomCreate, RoomUpdate

class CRUDRoom(CRUDBase[Room, RoomCreate, RoomUpdate]):
    pass

room = CRUDRoom(Room)
