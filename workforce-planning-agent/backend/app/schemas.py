from pydantic import BaseModel
from typing import Optional

class AdvisorQuery(BaseModel):
    query: str

class ScenarioCreate(BaseModel):
    scenario_name: str
    description: str = ""
    scenario_type: str = "Baseline"
    assumptions: str = "{}"
    created_by: str = "demo-user"

class SettingsPayload(BaseModel):
    attrition_weight_engagement: float = 1.0
    health_threshold_healthy: float = 0.9
