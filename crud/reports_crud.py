from sqlalchemy.orm import Session
from app import models, schemas

def create_report(db: Session, report: schemas.ReportCreate):
    db_report = models.Reports(**report.dict())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report

def get_report(db: Session, report_id: int):
    return db.query(models.Reports).filter(models.Reports.id == report_id).first()

def get_reports(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Reports).offset(skip).limit(limit).all()

def update_report(db: Session, report_id: int, report_update: schemas.ReportUpdate):
    db_report = db.query(models.Reports).filter(models.Reports.id == report_id).first()
    if not db_report:
        return None
    for key, value in report_update.dict(exclude_unset=True).items():
        setattr(db_report, key, value)
    db.commit()
    db.refresh(db_report)
    return db_report

def delete_report(db: Session, report_id: int):
    db_report = db.query(models.Reports).filter(models.Reports.id == report_id).first()
    if not db_report:
        return None
    db.delete(db_report)
    db.commit()
    return db_report

