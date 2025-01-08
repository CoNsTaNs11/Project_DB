from sqlalchemy.orm import Session
from app import models, schemas

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Events(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_event(db: Session, event_id: int):
    return db.query(models.Events).filter(models.Events.id == event_id).first()

def get_events(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Events).offset(skip).limit(limit).all()

def update_event(db: Session, event_id: int, event_update: schemas.EventUpdate):
    db_event = db.query(models.Events).filter(models.Events.id == event_id).first()
    if not db_event:
        return None
    for key, value in event_update.dict(exclude_unset=True).items():
        setattr(db_event, key, value)
    db.commit()
    db.refresh(db_event)
    return db_event

def delete_event(db: Session, event_id: int):
    db_event = db.query(models.Events).filter(models.Events.id == event_id).first()
    if not db_event:
        return None
    db.delete(db_event)
    db.commit()
    return db_event
