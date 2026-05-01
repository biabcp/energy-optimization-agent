def department_health(dep):
    pct = dep.current_headcount / dep.target_headcount if dep.target_headcount else 0
    if pct >= 0.9: status = "Healthy"
    elif pct >= 0.75: status = "Watch"
    elif pct >= 0.6: status = "At Risk"
    else: status = "Critical"
    return {"department": dep.department_name, "staffing_percentage": round(pct*100,1), "status": status,
            "headcount_gap": dep.target_headcount - dep.current_headcount - dep.open_requisitions}
