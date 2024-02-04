from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps
from uuid import UUID

router = APIRouter()

@router.post("/", response_model=schemas.Place)
def create_place(
    *,
    db: Session = Depends(deps.get_db),
    place_in: schemas.PlaceCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    place = crud.place.create(db=db, obj_in=place_in)
    return place

@router.put("/{id}", response_model=schemas.Place)
def update_place(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    place_in: schemas.PlaceUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    place = crud.place.get(db=db, id=id)
    if not place:
        raise HTTPException(status_code=404, detail="Place not found")
    place = crud.place.update(db=db, db_obj=place, obj_in=place_in)
    return place

@router.get("/{id}", response_model=schemas.Place)
def read_place(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    place = crud.place.get(db=db, id=id)
    if not place:
        raise HTTPException(status_code=404, detail="Place not found")
    return place

@router.delete("/{id}", response_model=schemas.Place)
def delete_place(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    place = crud.place.get(db=db, id=id)
    if not place:
        raise HTTPException(status_code=404, detail="Place not found")
    place = crud.place.remove(db=db, id=id)
    return place