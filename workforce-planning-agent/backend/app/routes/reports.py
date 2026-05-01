from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
router=APIRouter(prefix="/reports",tags=["reports"])
@router.get("/workforce-plan")
def wr(): return {"report":"# Workforce planning report"}
@router.get("/attrition-risk")
def ar(): return {"report":"# Attrition risk report"}
@router.get("/hiring-priorities")
def hr(): return {"report":"# Hiring priorities report"}
@router.get("/ai-readiness")
def ai(): return {"report":"# AI readiness report"}
@router.get("/department/{department_id}")
def dr(department_id:int): return {"report":f"# Department {department_id} report"}
