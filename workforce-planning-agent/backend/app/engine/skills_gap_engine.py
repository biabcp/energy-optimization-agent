AI_SKILLS={"AI Literacy","Data Governance","Data Engineering","Prompt Engineering","AI Risk Management","Model Evaluation","Cloud AI Services","Automation Design","Responsible AI","Cybersecurity for AI Systems"}

def skill_gap(skill):
    return {"skill_name":skill.skill_name,"gap_size":skill.target_employee_count-skill.current_employee_count,
    "current":skill.current_employee_count,"target":skill.target_employee_count,"is_ai_readiness":skill.skill_name in AI_SKILLS}
