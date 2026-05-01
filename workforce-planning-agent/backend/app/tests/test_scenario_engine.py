from app.engine.scenario_engine import run_scenario

def test_scenario(): assert run_scenario(75,1000,'{"planned_hires":2,"attrition":1}')['projected_headcount']==76
