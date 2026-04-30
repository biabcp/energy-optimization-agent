from app.analytics.cost_estimator import estimate_costs

def test_costs():
    c=estimate_costs(100,50,0.1,10)
    assert c['monthly_cost']>0 and c['potential_savings']>0
