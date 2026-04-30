from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter()

@router.get('/machines', response_model=list[schemas.MachineOut])
def get_machines(db: Session = Depends(get_db)):
    return db.query(models.Machine).all()

@router.post('/machines', response_model=schemas.MachineOut)
def create_machine(machine: schemas.MachineCreate, db: Session = Depends(get_db)):
    m = models.Machine(**machine.model_dump())
    db.add(m); db.commit(); db.refresh(m)
    return m
