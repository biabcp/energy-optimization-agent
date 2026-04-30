from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from ..database import get_db
from .energy import summary, anomalies
from .recommendations import get_recommendations

router = APIRouter()

@router.get('/reports/markdown')
def report_markdown(db: Session = Depends(get_db)):
    s = summary(db)
    a = anomalies(db)
    r = get_recommendations(db)
    md = f"# Energy Optimization Report\n\n## Executive Summary\nTotal usage: {s.get('total_kwh',0)} kWh\nEstimated monthly cost: ${s.get('estimated_cost',0)}\n\n## Top Consuming Machines\n"
    for k,v in s.get('top_machines',{}).items(): md += f"- {k}: {v:.1f} kWh\n"
    md += "\n## Anomalies\n"
    for i in a[:10]: md += f"- {i['machine_name']} ({i['severity']}): {i['explanation']}\n"
    md += "\n## Recommendations\n"
    for i in r[:10]: md += f"- **{i['title']}** ({i['priority']}): {i['recommended_action']}\n"
    md += f"\n## Estimated Savings\nPotential monthly savings: ${s.get('monthly_savings_opportunity',0)}\n"
    return Response(content=md, media_type='text/markdown')
