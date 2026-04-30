import pandas as pd
from app.analytics.anomaly_detection import detect_anomalies

def test_detects_spike():
    vals=[10]*30+[50]
    df=pd.DataFrame({'machine_id':['M1']*31,'machine_name':['X']*31,'timestamp':pd.date_range('2026-01-01',periods=31,freq='h'),'current_power_kw':vals,'utilization_percent':[50]*31})
    out=detect_anomalies(df)
    assert not out.empty
