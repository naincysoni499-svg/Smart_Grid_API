from fastapi import FastAPI
from database import engine, SessionLocal
from models import Base, SmartMeterData
from schemas import MeterData
from tasks import calculate_total_load

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Smart Grid API is Running"}


@app.post("/telemetry")
def add_data(data: MeterData):
    db = SessionLocal()

    try:
        meter = SmartMeterData(
            meter_id=data.meter_id,
            city_zone=data.city_zone,
            timestamp=data.timestamp,
            power_usage=data.power_usage,
            voltage=data.voltage,
            current=data.current,
            frequency=data.frequency
        )

        db.add(meter)
        db.commit()
        db.refresh(meter)

        # Uncomment this after the API works correctly
        calculate_total_load.delay()

        return {
            "message": "Telemetry data stored successfully",
            "data": {
                "meter_id": meter.meter_id,
                "city_zone": meter.city_zone
            }
        }

    except Exception as e:
        db.rollback()
        return {
            "error": str(e)
        }

    finally:
        db.close()