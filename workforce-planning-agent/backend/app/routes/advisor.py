from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
router=APIRouter(prefix="/advisor",tags=["advisor"])
from ..schemas import AdvisorQuery
@router.post("/query")
def q(payload:AdvisorQuery,db:Session=Depends(get_db)):
 from ..engine.workforce_advisor_engine import answer
 context={"understaffed":"Engineering and Customer Operations are most understaffed.","attrition":"Engineering has highest high-risk concentration.","hiring":"Prioritize Security Engineer and Senior Data Engineer.","budget":"Sales and Customer Operations are currently over budget.","skills":"Top AI skill gaps: Prompt Engineering, Model Evaluation, Responsible AI."}
 return {"answer":answer(payload.query,context),"disclaimer":"Decision-support only."}
