from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from datetime import datetime
from .database import Base

class Employee(Base):
    __tablename__ = "employees"
    employee_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String); last_name = Column(String); email = Column(String, unique=True)
    department = Column(String); job_title = Column(String); role_family = Column(String); manager = Column(String)
    location = Column(String); employment_type = Column(String); employee_level = Column(String)
    hire_date = Column(String); tenure_months = Column(Integer); compensation = Column(Float)
    performance_rating = Column(Float); engagement_score = Column(Float); promotion_readiness = Column(String)
    flight_risk = Column(String); status = Column(String, default="Active")

class Department(Base):
    __tablename__ = "departments"
    department_id = Column(Integer, primary_key=True); department_name = Column(String, unique=True)
    leader = Column(String); current_headcount = Column(Integer); approved_headcount = Column(Integer)
    target_headcount = Column(Integer); budget = Column(Float); current_compensation_spend = Column(Float)
    open_requisitions = Column(Integer); priority_level = Column(String)

class Role(Base):
    __tablename__ = "roles"
    role_id = Column(Integer, primary_key=True); role_title = Column(String); role_family = Column(String)
    department = Column(String); current_count = Column(Integer); target_count = Column(Integer)
    open_requisitions = Column(Integer); criticality = Column(String); average_compensation = Column(Float)
    required_skills = Column(Text)

class Skill(Base):
    __tablename__ = "skills"
    skill_id = Column(Integer, primary_key=True); skill_name = Column(String, unique=True); category = Column(String)
    strategic_importance = Column(String); current_employee_count = Column(Integer); target_employee_count = Column(Integer)
    gap_size = Column(Integer)

class AttritionRisk(Base):
    __tablename__ = "attrition_risks"
    risk_id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.employee_id'))
    risk_score = Column(Integer); risk_level = Column(String); risk_factors = Column(Text)
    recommended_action = Column(Text); generated_at = Column(DateTime, default=datetime.utcnow)

class Requisition(Base):
    __tablename__ = "requisitions"
    requisition_id = Column(Integer, primary_key=True); role_title = Column(String); department = Column(String)
    hiring_manager = Column(String); priority = Column(String); status = Column(String)
    target_start_date = Column(String); estimated_compensation = Column(Float); business_justification = Column(Text)

class WorkforceScenario(Base):
    __tablename__ = "scenarios"
    scenario_id = Column(Integer, primary_key=True); scenario_name = Column(String); description = Column(Text)
    created_by = Column(String); scenario_type = Column(String); assumptions = Column(Text)
    projected_headcount = Column(Integer); projected_budget = Column(Float); projected_gap_reduction = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True)
    action = Column(String); details = Column(Text); created_at = Column(DateTime, default=datetime.utcnow)
