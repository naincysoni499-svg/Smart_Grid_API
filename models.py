from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from datetime import datetime

class SmartMeterData(Base):
    __tablename__ = "smart_meter_data"

    id = Column(Integer, primary_key=True, index=True)
    meter_id = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    power_usage = Column(Float)
    voltage = Column(Float)
    current = Column(Float)
    frequency = Column(Float)