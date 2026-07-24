from celery_worker import celery
from database import SessionLocal
from models import SmartMeterData, ZoneLoadReport
from datetime import datetime

@celery.task
def calculate_total_load():
    db = SessionLocal()

    data = db.query(SmartMeterData).all()

    total_load = {}

    for meter in data:
        zone = meter.city_zone

        if zone not in total_load:
            total_load[zone] = 0

        total_load[zone] += meter.power_usage

    # Clear old report
    db.query(ZoneLoadReport).delete()

    # Save new report
    for zone, load in total_load.items():
        report = ZoneLoadReport(
            city_zone=zone,
            total_load=load,
            timestamp=datetime.utcnow()
        )

        db.add(report)

    db.commit()
    db.close()

    print("Zone Load Report Updated Successfully")

    return "Aggregation Completed"