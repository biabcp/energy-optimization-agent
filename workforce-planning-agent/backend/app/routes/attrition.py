from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
router=APIRouter(prefix="/attrition",tags=["attrition"])
@router.get("/summary")
def summary(): return {"message":"run /attrition/recalculate"}
@router.get("/high-risk")
def high(db:Session=Depends(get_db)): return db.query(models.AttritionRisk).filter(models.AttritionRisk.risk_score>=61).all()
@router.get("/by-department")
def by_dep(): return []
@router.post("/recalculate")
def recalc(db:Session=Depends(get_db)):
 from ..engine.attrition_risk_engine import score_employee
 db.query(models.AttritionRisk).delete();
 for e in db.query(models.Employee).all():
  s,l,f=score_employee(e); db.add(models.AttritionRisk(employee_id=e.employee_id,risk_score=s,risk_level=l,risk_factors=", ".join(f),recommended_action="Stay interview and growth plan"));
 db.commit(); return {"status":"recalculated"}
