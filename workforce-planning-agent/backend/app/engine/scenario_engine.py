import json

def run_scenario(base_headcount, base_budget, assumptions):
    a=json.loads(assumptions or "{}")
    hires=a.get("planned_hires",0); attr=a.get("attrition",0); mult=a.get("comp_multiplier",1.0)
    return {"projected_headcount":base_headcount+hires-attr,"projected_budget":round(base_budget*mult,2),"projected_gap_reduction":max(0,hires-attr)}
