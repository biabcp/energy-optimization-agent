from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
router=APIRouter(prefix="/settings",tags=["settings"])
_settings={"attrition_weight_engagement":1.0,"health_threshold_healthy":0.9}
@router.get("")
def get_settings(): return _settings
@router.post("")
def set_settings(payload:dict): _settings.update(payload); return _settings
