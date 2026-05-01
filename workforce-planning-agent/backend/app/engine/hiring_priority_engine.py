CRIT={"Low":5,"Medium":12,"High":18,"Critical":25}
def score(role, dep_gap, attrition_exposure=10, skills_gap=8, business_priority=8, budget_feasible=10):
    headcount_points=min(20,max(0,dep_gap*3)); criticality=CRIT.get(role.criticality,10)
    total=min(100,criticality+headcount_points+attrition_exposure+skills_gap+business_priority+budget_feasible)
    return total
