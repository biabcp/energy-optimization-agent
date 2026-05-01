from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
router=APIRouter(prefix="/roles",tags=["roles"])
@router.get("")
def list_roles(): return []
@router.get("/gaps")
def gaps(): return []
@router.get("/critical")
def critical(): return []
