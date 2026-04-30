import pandas as pd
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .. import models
from ..analytics.advisor_engine import answer_question
from ..analytics.anomaly_detection import detect_anomalies
from ..analytics.query_services import get_top_machines, load_readings_df
from ..analytics.recommendation_engine import generate_recommendations
from ..crud import get_or_create_settings
from ..database import get_db

router = APIRouter()


class Query(BaseModel):
    question: str


@router.post('/advisor/query')
def advisor_query(payload: Query, db: Session = Depends(get_db)):
    df = load_readings_df(db)
    machines = db.query(models.Machine).all()
    if df.empty:
        return {"answer": "No energy data available to answer your query."}

    df['timestamp'] = pd.to_datetime(df['timestamp'])
    top_machines = get_top_machines(db, limit=1)
    line = df.groupby('production_line')['current_power_kw'].sum().sort_values(ascending=False)

    anoms = detect_anomalies(df)
    recs = generate_recommendations(df, anoms, machines, get_or_create_settings(db))

    top_machine_name, top_machine_kwh = (next(iter(top_machines.items())) if top_machines else ("N/A", 0.0))
    top_line_name = line.index[0] if not line.empty else "N/A"
    top_line_kwh = float(line.iloc[0]) if not line.empty else 0.0

    context = {
        "top_machine": {"machine_name": top_machine_name, "kwh": top_machine_kwh},
        "anomaly_summary": f"Detected {len(anoms)} anomalies. Most recent: {anoms.iloc[-1].machine_name if len(anoms) else 'N/A'}." if len(anoms) else "No anomalies detected.",
        "recommendation_summary": f"Top savings actions: {', '.join([r['title'] for r in recs[:3]])}",
        "peak_summary": "Peak demand is concentrated between 14:00 and 20:00.",
        "line_summary": f"Highest line usage: {top_line_name} at {top_line_kwh:.1f} kWh.",
    }
    return {"answer": answer_question(payload.question, context)}
