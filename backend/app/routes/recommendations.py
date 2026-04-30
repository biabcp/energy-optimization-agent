import pandas as pd
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import models
from ..analytics.anomaly_detection import detect_anomalies
from ..analytics.query_services import load_readings_df
from ..analytics.recommendation_engine import generate_recommendations
from ..crud import get_or_create_settings
from ..database import get_db

router = APIRouter()


@router.get('/recommendations')
def get_recommendations(db: Session = Depends(get_db)):
    df = load_readings_df(db)
    machines = db.query(models.Machine).all()
    if df.empty:
        return []
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    anoms = detect_anomalies(df)
    settings = get_or_create_settings(db)
    return generate_recommendations(df, anoms, machines, settings)
