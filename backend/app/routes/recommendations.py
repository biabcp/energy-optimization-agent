import pandas as pd
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..analytics.anomaly_detection import detect_anomalies
from ..analytics.recommendation_engine import generate_recommendations
from ..crud import get_or_create_settings

router = APIRouter()

@router.get('/recommendations')
def get_recommendations(db: Session = Depends(get_db)):
    rows = db.query(models.EnergyReading).all()
    machines = db.query(models.Machine).all()
    df = pd.DataFrame([{"timestamp":r.timestamp,"machine_id":r.machine_id,"machine_name":r.machine_name,"production_line":r.production_line,"machine_type":r.machine_type,"current_power_kw":r.current_power_kw,"utilization_percent":r.utilization_percent,"units_produced":r.units_produced} for r in rows])
    if df.empty: return []
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    anoms = detect_anomalies(df)
    settings = get_or_create_settings(db)
    return generate_recommendations(df, anoms, machines, settings)
