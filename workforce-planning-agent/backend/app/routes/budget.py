from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
router=APIRouter(prefix="/budget",tags=["budget"])
@router.get("/summary")
def summary(db:Session=Depends(get_db)):
 from ..engine.budget_engine import summarize
 return summarize(db.query(models.Department).all())
@router.get("/by-department")
def by_dep(db:Session=Depends(get_db)): return [{"department":d.department_name,"budget":d.budget,"spend":d.current_compensation_spend} for d in db.query(models.Department).all()]
@router.post("/project-hiring-plan")
def proj(payload:dict): return {"status":"projected","input":payload}
