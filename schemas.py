from pydantic import BaseModel
from datetime import datetime

class MeterData(BaseModel):
    meter_id: str
    timestamp: datetime
    power_usage: float
    voltage: float
    current: float
    frequency: float