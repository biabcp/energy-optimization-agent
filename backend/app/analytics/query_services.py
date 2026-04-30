from __future__ import annotations

import pandas as pd
from sqlalchemy import func
from sqlalchemy.orm import Session

from .. import models


def load_readings_df(db: Session) -> pd.DataFrame:
    rows = db.query(models.EnergyReading).all()
    return pd.DataFrame(
        [
            {
                "timestamp": r.timestamp,
                "machine_id": r.machine_id,
                "machine_name": r.machine_name,
                "production_line": r.production_line,
                "machine_type": r.machine_type,
                "current_power_kw": r.current_power_kw,
                "utilization_percent": r.utilization_percent,
                "units_produced": r.units_produced,
            }
            for r in rows
        ]
    )


def get_top_machines(db: Session, limit: int = 5) -> dict[str, float]:
    top_rows = (
        db.query(
            models.EnergyReading.machine_name,
            func.sum(models.EnergyReading.current_power_kw).label("total_kw"),
        )
        .group_by(models.EnergyReading.machine_name)
        .order_by(func.sum(models.EnergyReading.current_power_kw).desc())
        .limit(limit)
        .all()
    )
    return {row.machine_name: float(row.total_kw) for row in top_rows}
