from datetime import datetime
from pydantic import BaseModel


class MachineCreate(BaseModel):
    machine_id: str
    machine_name: str
    production_line: str
    machine_type: str
    status: str
    rated_power_kw: float


class MachineOut(MachineCreate):
    id: int

    class Config:
        from_attributes = True


class SettingSchema(BaseModel):
    electricity_rate: float
    demand_charge_rate: float
    operating_hours_per_day: float
    peak_start_hour: int
    peak_end_hour: int


class EnergyOut(BaseModel):
    timestamp: datetime
    machine_id: str
    machine_name: str
    production_line: str
    machine_type: str
    current_power_kw: float
    utilization_percent: float
    units_produced: int

    class Config:
        from_attributes = True
