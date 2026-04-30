from . import models


def get_or_create_settings(db):
    s = db.query(models.Setting).first()
    if not s:
        s = models.Setting()
        db.add(s)
        db.commit()
        db.refresh(s)
    return s
