def score_employee(e):
    score = 0; factors=[]
    if e.engagement_score < 60: score += 25; factors.append("Low engagement")
    if e.tenure_months > 48 and e.promotion_readiness == "Low": score += 10; factors.append("Stalled growth")
    if e.flight_risk == "High": score += 25; factors.append("High flight risk signal")
    if e.performance_rating >= 4 and e.engagement_score < 70: score += 15; factors.append("High performer disengagement")
    score=min(100,score)
    level = "Low" if score<=30 else "Medium" if score<=60 else "High" if score<=80 else "Critical"
    return score, level, factors
