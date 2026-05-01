from app.engine.skills_gap_engine import skill_gap
class S: skill_name='Prompt Engineering'; current_employee_count=2; target_employee_count=7
def test_skill_gap(): assert skill_gap(S)['gap_size']==5
