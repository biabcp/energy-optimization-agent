from sqlalchemy.orm import Session
from . import models

def log(db: Session, action: str, details: str):
    db.add(models.AuditLog(action=action, details=details)); db.commit()
