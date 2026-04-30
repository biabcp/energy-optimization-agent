# Energy Optimization Agent MVP

Vendor-neutral manufacturing energy optimization app (FastAPI + React + SQLite).

## Why this matters
Manufacturing plants can reduce utility spend and downtime by monitoring machine-level consumption, detecting spikes, and acting on recommendations.

## Architecture
Frontend (React/Vite) -> FastAPI API -> SQLite
Analytics modules: anomaly detection, cost estimator, recommendation engine, advisor engine.

## Setup
### Docker Compose
`docker compose up --build`

### Backend local
`cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload`

### Frontend local
`cd frontend && npm install && npm run dev`

## Sample CSV format
Columns: timestamp,machine_id,machine_name,production_line,machine_type,current_power_kw,utilization_percent,units_produced

## API endpoints
/health, /machines, /energy, /energy/upload, /analytics/summary, /analytics/anomalies, /recommendations, /advisor/query, /reports/markdown, /settings

## Roadmap
- stronger statistical models
- PDF rendering polish
- auth/roles
- IoT connectors (SCADA/MES/ERP/CMMS)

## Screenshots
- Dashboard: TODO
- Advisor: TODO
