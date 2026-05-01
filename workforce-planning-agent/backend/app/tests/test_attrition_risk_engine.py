from app.engine.attrition_risk_engine import score_employee
class E: engagement_score=50; tenure_months=60; promotion_readiness='Low'; flight_risk='High'; performance_rating=4

def test_score():
    s,l,f=score_employee(E); assert s>60 and l in ['High','Critical'] and f
