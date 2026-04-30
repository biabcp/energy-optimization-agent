import pandas as pd
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..analytics.anomaly_detection import detect_anomalies
from ..analytics.advisor_engine import answer_question
from ..analytics.recommendation_engine import generate_recommendations
from ..crud import get_or_create_settings

router = APIRouter()

class Query(BaseModel):
    question: str

@router.post('/advisor/query')
def advisor_query(payload: Query, db: Session = Depends(get_db)):
    rows = db.query(models.EnergyReading).all(); machines = db.query(models.Machine).all()
    df = pd.DataFrame([{"timestamp":r.timestamp,"machine_id":r.machine_id,"machine_name":r.machine_name,"production_line":r.production_line,"machine_type":r.machine_type,"current_power_kw":r.current_power_kw,"utilization_percent":r.utilization_percent,"units_produced":r.units_produced} for r in rows])
    df['timestamp']=pd.to_datetime(df['timestamp'])
    top = df.groupby('machine_name')['current_power_kw'].sum().sort_values(ascending=False)
    anoms = detect_anomalies(df)
    recs = generate_recommendations(df, anoms, machines, get_or_create_settings(db))
    line = df.groupby('production_line')['current_power_kw'].sum().sort_values(ascending=False)
    context = {
      "top_machine": {"machine_name": top.index[0], "kwh": float(top.iloc[0])},
      "anomaly_summary": f"Detected {len(anoms)} anomalies. Most recent: {anoms.iloc[-1].machine_name if len(anoms) else 'N/A'}." if len(anoms) else "No anomalies detected.",
      "recommendation_summary": f"Top savings actions: {', '.join([r['title'] for r in recs[:3]])}",
      "peak_summary": "Peak demand is concentrated between 14:00 and 20:00.",
      "line_summary": f"Highest line usage: {line.index[0]} at {line.iloc[0]:.1f} kWh."
    }
    return {"answer": answer_question(payload.question, context)}
