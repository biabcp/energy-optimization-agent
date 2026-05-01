from app.engine.budget_engine import summarize
class D:
    def __init__(self,b,s): self.budget=b; self.current_compensation_spend=s

def test_budget(): assert summarize([D(100,90)])['status']=='Under budget'
