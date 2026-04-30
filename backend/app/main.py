from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine, SessionLocal
from .routes import machines, energy, recommendations, advisor, reports
from . import models
from .seed_data import seed

app = FastAPI(title="Energy Optimization Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with ["http://localhost:5173"] in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
with SessionLocal() as db:
    if not db.query(models.Setting).first():
        db.add(models.Setting())
        db.commit()
    seed(db)

app.include_router(machines.router)
app.include_router(energy.router)
app.include_router(recommendations.router)
app.include_router(advisor.router)
app.include_router(reports.router)


@app.get("/health")
def health():
    return {"status": "ok"}
