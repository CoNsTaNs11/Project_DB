from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return crud.events.create_event(db, event)

@router.get("/{event_id}", response_model=schemas.Event)
def read_event(event_id: int, db: Session = Depends(get_db)):
    db_event = crud.events.get_event(db, event_id)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

@router.get("/", response_model=list[schemas.Event])
def read_events(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.events.get_events(db, skip, limit)

@router.put("/{event_id}", response_model=schemas.Event)
def update_event(event_id: int, event_update: schemas.EventUpdate, db: Session = Depends(get_db)):
    db_event = crud.events.update_event(db, event_id, event_update)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

@router.delete("/{event_id}", response_model=schemas.Event)
def delete_event(event_id: int, db: Session = Depends(get_db)):
    db_event = crud.events.delete_event(db, event_id)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event
