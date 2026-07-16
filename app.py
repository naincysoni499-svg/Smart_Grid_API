from fastapi import FastAPI
from database import engine, SessionLocal
from models import Base, SmartMeterData
from schemas import MeterData

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Grid API is Running"}

@app.post("/telemetry")
def add_data(data: MeterData):
    db = SessionLocal()

    meter = SmartMeterData(
        meter_id=data.meter_id,
        timestamp=data.timestamp,
        power_usage=data.power_usage,
        voltage=data.voltage,
        current=data.current,
        frequency=data.frequency
    )

    db.add(meter)
    db.commit()
    db.close()

    return {"message": "Telemetry data stored successfully"}