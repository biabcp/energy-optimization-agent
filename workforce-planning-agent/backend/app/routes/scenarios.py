from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
router=APIRouter(prefix="/scenarios",tags=["scenarios"])
@router.get("")
def list_s(db:Session=Depends(get_db)): return db.query(models.WorkforceScenario).all()
@router.post("")
def create(payload:dict,db:Session=Depends(get_db)): s=models.WorkforceScenario(**payload); db.add(s); db.commit(); db.refresh(s); return s
@router.get("/{scenario_id}")
def get_s(scenario_id:int,db:Session=Depends(get_db)): return db.query(models.WorkforceScenario).filter(models.WorkforceScenario.scenario_id==scenario_id).first()
@router.post("/{scenario_id}/run")
def run(scenario_id:int,db:Session=Depends(get_db)):
 from ..engine.scenario_engine import run_scenario
 s=db.query(models.WorkforceScenario).filter(models.WorkforceScenario.scenario_id==scenario_id).first(); return run_scenario(75,15350000,s.assumptions or "{}")
@router.post("/compare")
def comp(payload:dict): return payload
