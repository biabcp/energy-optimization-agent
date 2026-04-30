from sqlalchemy import Column, DateTime, Float, Integer, String, Text

from .database import Base


class Machine(Base):
    __tablename__ = "machines"
    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(String, unique=True, index=True)
    machine_name = Column(String)
    production_line = Column(String, index=True)
    machine_type = Column(String, index=True)
    status = Column(String, default="running")
    rated_power_kw = Column(Float)


class EnergyReading(Base):
    __tablename__ = "energy_readings"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, index=True)
    machine_id = Column(String, index=True)
    machine_name = Column(String)
    production_line = Column(String, index=True)
    machine_type = Column(String)
    current_power_kw = Column(Float)
    utilization_percent = Column(Float)
    units_produced = Column(Integer, default=0)


class Setting(Base):
    __tablename__ = "settings"
    id = Column(Integer, primary_key=True)
    electricity_rate = Column(Float, default=0.12)
    demand_charge_rate = Column(Float, default=12.0)
    operating_hours_per_day = Column(Float, default=16.0)
    peak_start_hour = Column(Integer, default=14)
    peak_end_hour = Column(Integer, default=20)


class Recommendation(Base):
    __tablename__ = "recommendations"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    reason = Column(Text)
    estimated_impact = Column(String)
    priority = Column(String)
    affected_asset = Column(String)
    recommended_action = Column(Text)
