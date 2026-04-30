from datetime import datetime, timedelta
import random
from . import models

MACHINES = [
    ("M001", "CNC Mill 01", "Line 1", "CNC", 55),
    ("M002", "Injection Molder 02", "Line 1", "Molder", 75),
    ("M003", "Packaging Line A", "Line 2", "Packaging", 30),
    ("M004", "Conveyor System B", "Line 2", "Conveyor", 25),
    ("M005", "Air Compressor 01", "Line 3", "Compressor", 60),
    ("M006", "Industrial Oven 03", "Line 3", "Oven", 80),
    ("M007", "Robotic Welder 02", "Line 1", "Welder", 50),
    ("M008", "Cooling Pump 01", "Line 2", "Pump", 28),
]

def seed(db):
    if db.query(models.EnergyReading).first():
        return
    for m in MACHINES:
        db.add(models.Machine(machine_id=m[0], machine_name=m[1], production_line=m[2], machine_type=m[3], rated_power_kw=m[4], status="running"))
    db.commit()

    start = datetime.utcnow() - timedelta(days=14)
    anomaly_slots = set(random.sample(range(14*24*8), 10))
    idx = 0
    for h in range(14*24):
        ts = start + timedelta(hours=h)
        for m in MACHINES:
            rated = m[4]
            peak_boost = 1.2 if 14 <= ts.hour <= 20 else 0.85
            util = random.randint(5, 95)
            base = rated * (0.25 + util/100*0.7) * peak_boost
            if m[0] in ["M005", "M008"] and util < 15:
                base = max(base, rated*0.3)
            if idx in anomaly_slots:
                base *= random.uniform(1.8, 2.5)
            db.add(models.EnergyReading(timestamp=ts, machine_id=m[0], machine_name=m[1], production_line=m[2], machine_type=m[3], current_power_kw=round(base,2), utilization_percent=util, units_produced=max(0,int(util*random.uniform(0.5,2.0)))))
            idx += 1
    db.commit()
