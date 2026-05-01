from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
router=APIRouter(prefix="/headcount",tags=["headcount"])
@router.get("/summary")
def summary(db:Session=Depends(get_db)):
 deps=db.query(models.Department).all(); return {"current_headcount":sum(d.current_headcount for d in deps),"approved_headcount":sum(d.approved_headcount for d in deps),"target_headcount":sum(d.target_headcount for d in deps),"open_requisitions":sum(d.open_requisitions for d in deps)}
@router.get("/by-department")
def by_dep(db:Session=Depends(get_db)):
 from ..engine.headcount_engine import department_health
 return [department_health(d) for d in db.query(models.Department).all()]
@router.get("/gaps")
def gaps(db:Session=Depends(get_db)): return [{"department":d.department_name,"gap":d.target_headcount-d.current_headcount-d.open_requisitions} for d in db.query(models.Department).all()]
