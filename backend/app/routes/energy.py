from io import StringIO

import pandas as pd
from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from .. import models, schemas
from ..analytics.anomaly_detection import detect_anomalies
from ..analytics.cost_estimator import estimate_costs
from ..analytics.query_services import get_top_machines, load_readings_df
from ..crud import get_or_create_settings
from ..database import get_db

router = APIRouter()


@router.get('/energy', response_model=list[schemas.EnergyOut])
def get_energy(db: Session = Depends(get_db)):
    return db.query(models.EnergyReading).order_by(models.EnergyReading.timestamp.desc()).limit(1000).all()


@router.post('/energy/upload')
async def upload_energy(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = (await file.read()).decode('utf-8')
    df = pd.read_csv(StringIO(content), parse_dates=['timestamp'])
    readings = df.to_dict(orient='records')
    db.bulk_insert_mappings(models.EnergyReading, readings)
    db.commit()
    return {"rows": len(df)}


@router.get('/analytics/anomalies')
def anomalies(db: Session = Depends(get_db)):
    df = load_readings_df(db)
    if df.empty:
        return []
    out = detect_anomalies(df)
    return out.sort_values('timestamp', ascending=False).head(100).to_dict(orient='records')


@router.get('/analytics/summary')
def summary(db: Session = Depends(get_db)):
    df = load_readings_df(db)
    settings = get_or_create_settings(db)
    if df.empty:
        return {}
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    total_kwh = float(df.current_power_kw.sum())
    peak_kw = float(df.current_power_kw.max())
    days = (df['timestamp'].max() - df['timestamp'].min()).days
    days = days if days > 0 else 1
    costs = estimate_costs(total_kwh / days, peak_kw, settings.electricity_rate, settings.demand_charge_rate)

    top = get_top_machines(db, limit=5)
    peak_periods = df.groupby(df.timestamp.dt.hour)['current_power_kw'].mean().sort_values(ascending=False).head(3)
    return {"total_kwh": round(total_kwh, 2), "estimated_cost": costs['monthly_cost'], "peak_demand_periods": peak_periods.to_dict(), "top_machines": top, "monthly_savings_opportunity": costs['potential_savings']}


@router.get('/settings', response_model=schemas.SettingSchema)
def get_settings(db: Session = Depends(get_db)):
    return get_or_create_settings(db)


@router.post('/settings', response_model=schemas.SettingSchema)
def save_settings(payload: schemas.SettingSchema, db: Session = Depends(get_db)):
    s = get_or_create_settings(db)
    for k, v in payload.model_dump().items():
        setattr(s, k, v)
    db.commit()
    db.refresh(s)
    return s
