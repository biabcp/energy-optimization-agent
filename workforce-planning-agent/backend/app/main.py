from fastapi import FastAPI
from .database import Base, engine, SessionLocal
from . import models
from .seed_data import seed
from .routes import employees, departments, roles, skills, headcount, attrition, hiring, budget, scenarios, advisor, reports, settings

app=FastAPI(title="workforce-planning-agent")
Base.metadata.create_all(bind=engine)
with SessionLocal() as db: seed(db)

@app.get('/health')
def health(): return {"status":"ok"}

for rt in [employees.router,departments.router,roles.router,skills.router,headcount.router,attrition.router,hiring.router,budget.router,scenarios.router,advisor.router,reports.router,settings.router]: app.include_router(rt)
