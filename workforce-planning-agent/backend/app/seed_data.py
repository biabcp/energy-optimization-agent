from sqlalchemy.orm import Session
from . import models

def seed(db: Session):
    if db.query(models.Department).first(): return
    deps=[("Engineering",20,24,28,4200000,3900000,4,"High"),("Product",8,10,12,1800000,1700000,2,"High"),("Cybersecurity",6,8,10,1600000,1550000,2,"Critical"),("Data & Analytics",9,10,12,1900000,1800000,2,"High"),("Finance",7,8,8,1200000,1100000,1,"Medium"),("HR / People Operations",6,7,8,950000,900000,1,"Medium"),("Sales",12,14,16,2300000,2400000,2,"High"),("Customer Operations",7,9,11,1400000,1450000,1,"High")]
    for i,d in enumerate(deps,1): db.add(models.Department(department_id=i,department_name=d[0],leader=f"Leader {i}",current_headcount=d[1],approved_headcount=d[2],target_headcount=d[3],budget=d[4],current_compensation_spend=d[5],open_requisitions=d[6],priority_level=d[7]))
    for i in range(1,76):
        dep=deps[(i-1)%8][0]
        db.add(models.Employee(employee_id=i,first_name=f"Emp{i}",last_name="Demo",email=f"emp{i}@demo.local",department=dep,job_title="Software Engineer" if dep=="Engineering" else "Analyst",role_family="Engineering",manager=f"Manager {(i%12)+1}",location="US",employment_type="Full-time",employee_level="L3",hire_date="2022-01-01",tenure_months=12+(i%60),compensation=80000+(i%8)*10000,performance_rating=2.5+(i%3),engagement_score=45+(i%50),promotion_readiness="Medium",flight_risk="High" if i%7==0 else "Medium" if i%9==0 else "Low",status="Active"))
    skills=["Python","SQL","Data Governance","Machine Learning","AI Risk Management","Cybersecurity","Cloud Infrastructure","Azure","AWS","SOC 2","ISO 27001","NIST CSF","Project Management","Agile Delivery","Financial Planning","Recruiting Operations","Workforce Planning","People Management","Customer Success","Business Analysis","Prompt Engineering","Responsible AI","Model Evaluation","Data Engineering","Change Management"]
    for i,s in enumerate(skills,1): db.add(models.Skill(skill_id=i,skill_name=s,category="AI / Machine Learning" if "AI" in s or s in ["Python","Data Engineering"] else "General",strategic_importance="High" if i%2==0 else "Medium",current_employee_count=3+(i%8),target_employee_count=8+(i%10),gap_size=0))
    db.commit()
