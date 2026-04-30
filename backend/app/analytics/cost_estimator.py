def estimate_costs(total_kwh: float, peak_kw: float, rate: float, demand_rate: float):
    daily = total_kwh * rate + peak_kw * demand_rate / 30
    weekly = daily * 7
    monthly = daily * 30
    potential_savings = monthly * 0.12
    return {
        "daily_cost": round(daily, 2),
        "weekly_cost": round(weekly, 2),
        "monthly_cost": round(monthly, 2),
        "potential_savings": round(potential_savings, 2),
    }
