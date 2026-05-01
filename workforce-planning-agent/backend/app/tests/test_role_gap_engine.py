from app.engine.role_gap_engine import role_gap
class R: role_title='a'; department='b'; target_count=5; current_count=2; open_requisitions=1; criticality='Critical'
def test_gap(): assert role_gap(R)['gap_size']==2
