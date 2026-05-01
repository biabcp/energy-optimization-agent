from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
router=APIRouter(prefix="/hiring",tags=["hiring"])
@router.get("/priorities")
def priorities(): return []
@router.get("/requisitions")
def reqs(db:Session=Depends(get_db)): return db.query(models.Requisition).all()
@router.post("/recommendations")
def rec(): return {"status":"generated"}
