import pandas as pd
from types import SimpleNamespace
from app.analytics.recommendation_engine import generate_recommendations

def test_idle_recommendation():
    df=pd.DataFrame([{'timestamp':pd.Timestamp('2026-01-01 15:00'),'machine_id':'M1','machine_name':'A','production_line':'Line 1','machine_type':'X','current_power_kw':30,'utilization_percent':5,'units_produced':1}])
    recs=generate_recommendations(df,pd.DataFrame(),[SimpleNamespace(machine_id='M1',rated_power_kw=100)],SimpleNamespace(peak_start_hour=14,peak_end_hour=20))
    assert any(r['title']=='Idle Load Waste' for r in recs)
