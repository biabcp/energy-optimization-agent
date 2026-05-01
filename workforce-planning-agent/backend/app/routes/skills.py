from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
router=APIRouter(prefix="/skills",tags=["skills"])
@router.get("")
def list_skills(db: Session=Depends(get_db)): return db.query(models.Skill).all()
@router.get("/gaps")
def gaps(db:Session=Depends(get_db)):
 from ..engine.skills_gap_engine import skill_gap
 return [skill_gap(s) for s in db.query(models.Skill).all()]
@router.get("/ai-readiness")
def ai(db:Session=Depends(get_db)):
 from ..engine.skills_gap_engine import skill_gap
 return [x for x in [skill_gap(s) for s in db.query(models.Skill).all()] if x["is_ai_readiness"]]
