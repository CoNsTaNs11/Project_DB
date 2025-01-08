from sqlalchemy.orm import Session
from app import models, schemas

def create_correspondent(db: Session, correspondent: schemas.CorrespondentCreate):
    db_correspondent = models.Correspondents(**correspondent.dict())
    db.add(db_correspondent)
    db.commit()
    db.refresh(db_correspondent)
    return db_correspondent

def get_correspondent(db: Session, correspondent_id: int):
    return db.query(models.Correspondents).filter(models.Correspondents.id == correspondent_id).first()

def get_correspondents(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Correspondents).offset(skip).limit(limit).all()

def update_correspondent(db: Session, correspondent_id: int, correspondent_update: schemas.CorrespondentUpdate):
    db_correspondent = db.query(models.Correspondents).filter(models.Correspondents.id == correspondent_id).first()
    if not db_correspondent:
        return None
    for key, value in correspondent_update.dict(exclude_unset=True).items():
        setattr(db_correspondent, key, value)
    db.commit()
    db.refresh(db_correspondent)
    return db_correspondent

def delete_correspondent(db: Session, correspondent_id: int):
    db_correspondent = db.query(models.Correspondents).filter(models.Correspondents.id == correspondent_id).first()
    if not db_correspondent:
        return None
    db.delete(db_correspondent)
    db.commit()
    return db_correspondent
