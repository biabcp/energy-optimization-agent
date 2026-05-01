# workforce-planning-agent

Local-first full-stack MVP for workforce planning with FastAPI + React + SQLite.

## Overview
Decision-support tool for headcount planning, attrition risk, role/skills gaps, hiring priorities, budget modeling, scenarios, and advisor Q&A.

## Setup
### Local
1. `cd workforce-planning-agent/backend && pip install -r requirements.txt`
2. `uvicorn app.main:app --reload`
3. `cd ../frontend && npm install && npm run dev`

### Docker
`docker compose up --build` from `workforce-planning-agent/`.

## API
Implements all required endpoint groups (`/employees`, `/departments`, `/roles`, `/skills`, `/headcount`, `/attrition`, `/hiring`, `/budget`, `/scenarios`, `/advisor`, `/reports`, `/settings`) and `/health`.

## Analytics logic
- Headcount formulas include gap and staffing health thresholds.
- Attrition scoring is deterministic and explainable.
- Hiring priority uses transparent weighted scoring.
- Budget modeling summarizes spend vs approved budget.
- Advisor uses keyword-matched deterministic responses.

## Testing
`cd backend && pytest`

## Screenshots
_Add screenshots here._

## Future roadmap
Workday/BambooHR/Greenhouse/ADP/Lattice integrations, Slack notifications, LLM advisor, RAG, org chart, succession, mobility matching, compensation analysis, Excel exports, board deck, multi-tenant SaaS.
