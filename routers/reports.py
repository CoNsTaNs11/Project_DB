from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Report)
def create_report(report: schemas.ReportCreate, db: Session = Depends(get_db)):
    return crud.reports.create_report(db, report)

@router.get("/{report_id}", response_model=schemas.Report)
def read_report(report_id: int, db: Session = Depends(get_db)):
    db_report = crud.reports.get_report(db, report_id)
    if not db_report:
        raise HTTPException(status_code=404, detail="Report not found")
    return db_report

@router.get("/", response_model=list[schemas.Report])
def read_reports(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.reports.get_reports(db, skip, limit)

@router.put("/{report_id}", response_model=schemas.Report)
def update_report(report_id: int, report_update: schemas.ReportUpdate, db: Session = Depends(get_db)):
    db_report = crud.reports.update_report(db, report_id, report_update)
    if not db_report:
        raise HTTPException(status_code=404, detail="Report not found")
    return db_report

@router.delete("/{report_id}", response_model=schemas.Report)
def delete_report(report_id: int, db: Session = Depends(get_db)):
    db_report = crud.reports.delete_report(db, report_id)
    if not db_report:
        raise HTTPException(status_code=404, detail="Report not found")
    return db_report
