def generate_recommendations(df, anomalies, machines, settings):
    recs = []
    rated_map = {m.machine_id: m.rated_power_kw for m in machines}

    if df.empty:
        return recs

    for _, r in df.iterrows():
        rated = rated_map.get(r.machine_id, 1)
        if r.utilization_percent < 10 and r.current_power_kw > 0.2 * rated:
            recs.append({
                "title": "Idle Load Waste",
                "reason": f"{r.machine_name} consumes power while mostly idle.",
                "estimated_impact": "$150-$500/month",
                "priority": "High",
                "affected_asset": r.machine_name,
                "recommended_action": "Enable auto-standby or shutdown during idle windows."
            })

    for _, a in anomalies.iterrows():
        if a.severity in ["Medium", "High"]:
            recs.append({
                "title": "Energy Spike Detected",
                "reason": a.explanation,
                "estimated_impact": "$100-$400/month",
                "priority": "Medium" if a.severity == "Medium" else "High",
                "affected_asset": a.machine_name,
                "recommended_action": "Inspect equipment and schedule preventive maintenance."
            })

    peak_hours = list(range(settings.peak_start_hour, settings.peak_end_hour + 1))
    peak_df = df[df.timestamp.dt.hour.isin(peak_hours)]
    if peak_df.empty:
        return recs[:20]

    top = peak_df.groupby("production_line")["current_power_kw"].sum().sort_values(ascending=False).head(1)
    if top.empty:
        return recs[:20]

    line = top.index[0]
    recs.append({
        "title": "Peak Demand Shift",
        "reason": f"{line} is driving high peak-hour demand.",
        "estimated_impact": "$300-$900/month",
        "priority": "High",
        "affected_asset": line,
        "recommended_action": "Shift heavy jobs outside peak demand window."
    })
    return recs[:20]
