from app.engine.hiring_priority_engine import score
class R: criticality='Critical'
def test_score(): assert score(R,4)>=60
