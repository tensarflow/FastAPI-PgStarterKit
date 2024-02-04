from typing import List
from uuid import UUID
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.place import Place
from app.schemas.place import PlaceCreate, PlaceUpdate

class CRUDPlace(CRUDBase[Place, PlaceCreate, PlaceUpdate]):
    pass

place = CRUDPlace(Place)