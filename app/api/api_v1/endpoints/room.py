from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps
from uuid import UUID

router = APIRouter()

@router.post("/", response_model=schemas.Room)
def create_room(
    *,
    db: Session = Depends(deps.get_db),
    room_in: schemas.RoomCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    room = crud.room.create(db=db, obj_in=room_in)
    return room

@router.put("/{id}", response_model=schemas.Room)
def update_room(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    room_in: schemas.RoomUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    room = crud.room.get(db=db, id=id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    room = crud.room.update(db=db, db_obj=room, obj_in=room_in)
    return room

@router.get("/{id}", response_model=schemas.Room)
def read_room(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    room = crud.room.get(db=db, id=id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@router.delete("/{id}", response_model=schemas.Room)
def delete_room(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    room = crud.room.get(db=db, id=id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    room = crud.room.remove(db=db, id=id)
    return room
