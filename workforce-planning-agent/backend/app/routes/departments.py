from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
router=APIRouter(prefix="/departments",tags=["departments"])
@router.get("")
def list_departments(db: Session=Depends(get_db)): return db.query(models.Department).all()
@router.get("/{department_id}")
def get_dep(department_id:int,db:Session=Depends(get_db)): return db.query(models.Department).filter(models.Department.department_id==department_id).first()
@router.get("/{department_id}/workforce-health")
def health(department_id:int,db:Session=Depends(get_db)):
 from ..engine.headcount_engine import department_health
 d=db.query(models.Department).filter(models.Department.department_id==department_id).first(); return department_health(d)
