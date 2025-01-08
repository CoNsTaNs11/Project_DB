from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Correspondent)
def create_correspondent(correspondent: schemas.CorrespondentCreate, db: Session = Depends(get_db)):
    return crud.correspondents.create_correspondent(db, correspondent)

@router.get("/{correspondent_id}", response_model=schemas.Correspondent)
def read_correspondent(correspondent_id: int, db: Session = Depends(get_db)):
    db_correspondent = crud.correspondents.get_correspondent(db, correspondent_id)
    if not db_correspondent:
        raise HTTPException(status_code=404, detail="Correspondent not found")
    return db_correspondent

@router.get("/", response_model=list[schemas.Correspondent])
def read_correspondents(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.correspondents.get_correspondents(db, skip, limit)

@router.put("/{correspondent_id}", response_model=schemas.Correspondent)
def update_correspondent(correspondent_id: int, correspondent_update: schemas.CorrespondentUpdate, db: Session = Depends(get_db)):
    db_correspondent = crud.correspondents.update_correspondent(db, correspondent_id, correspondent_update)
    if not db_correspondent:
        raise HTTPException(status_code=404, detail="Correspondent not found")
    return db_correspondent

@router.delete("/{correspondent_id}", response_model=schemas.Correspondent)
def delete_correspondent(correspondent_id: int, db: Session = Depends(get_db)):
    db_correspondent = crud.correspondents.delete_correspondent(db, correspondent_id)
    if not db_correspondent:
        raise HTTPException(status_code=404, detail="Correspondent not found")
    return db_correspondent
