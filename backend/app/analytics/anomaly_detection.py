import pandas as pd


def detect_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()
    df = df.sort_values(["machine_id", "timestamp"]).copy()
    df["rolling_mean"] = df.groupby("machine_id")["current_power_kw"].transform(lambda s: s.rolling(24, min_periods=6).mean())
    df["rolling_std"] = df.groupby("machine_id")["current_power_kw"].transform(lambda s: s.rolling(24, min_periods=6).std().fillna(0))
    df["threshold"] = df["rolling_mean"] + (2 * df["rolling_std"])
    anoms = df[df["current_power_kw"] > df["threshold"]].copy()
    if anoms.empty:
        return anoms
    anoms["z_score"] = (anoms["current_power_kw"] - anoms["rolling_mean"]) / anoms["rolling_std"].replace(0, 1)
    anoms["severity"] = anoms["z_score"].apply(lambda x: "High" if x > 3.5 else ("Medium" if x > 2.5 else "Low"))
    anoms["explanation"] = anoms.apply(
        lambda r: f"{r['machine_name']} drew {r['current_power_kw']:.1f} kW, above its typical {r['rolling_mean']:.1f} kW baseline.", axis=1
    )
    return anoms
