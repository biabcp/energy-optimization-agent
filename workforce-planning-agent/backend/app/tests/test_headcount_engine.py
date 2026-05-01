from app.engine.headcount_engine import department_health
class D: department_name='X'; current_headcount=9; target_headcount=10; open_requisitions=0

def test_health():
    assert department_health(D)['status']=='Healthy'
