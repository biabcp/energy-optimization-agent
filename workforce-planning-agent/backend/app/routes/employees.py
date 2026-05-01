from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
router=APIRouter(prefix="/employees",tags=["employees"])
@router.get("")
def list_employees(db: Session=Depends(get_db)): return db.query(models.Employee).all()
@router.get("/{employee_id}")
def get_employee(employee_id:int,db:Session=Depends(get_db)): return db.query(models.Employee).filter(models.Employee.employee_id==employee_id).first()
@router.post("")
def create_employee(payload:dict,db:Session=Depends(get_db)): return {"message":"stub"}
@router.put("/{employee_id}")
def update_employee(employee_id:int,payload:dict,db:Session=Depends(get_db)): return {"message":"updated","employee_id":employee_id}
