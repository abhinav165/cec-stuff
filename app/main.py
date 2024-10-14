from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import AverageMeasurements
import models
from database import engine, SessionLocal
from sqlalchemy import func
import redis
import json

# Create the FastAPI app
app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/populate_experiment_data")
def populate_experiment_data(db: Session = Depends(get_db)):
    # Connect to Redis
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    experiment_data = {
        "experiment_configured": {
            'experiment': '03113f5b-f19a-484b-a799-c3f5a0d432a5',
            'researcher': 'd.landau@uu.nl',
            'sensors': [
                'b007a37d-9626-4fb0-b970-8b3ac7d4ba5b',
                '3613db1c-e578-49b4-9f29-343008f1ec67'
            ],
            'temperature_range': {
                'upper_threshold': 26.5,
                'lower_threshold': 25.5
            }
        },
        "sensor_temperature_measured": [
            {
                'experiment': '03113f5b-f19a-484b-a799-c3f5a0d432a5',
                'sensor': 'b007a37d-9626-4fb0-b970-8b3ac7d4ba5b',
                'measurement_id': 'f6e1142f-b510-40e9-8851-ea750e8e944b',
                'timestamp': 1728586719.9010828,
                'temperature': 25.46674919128418,
            },
            {
                'experiment': '03113f5b-f19a-484b-a799-c3f5a0d432a5',
                'sensor': '3613db1c-e578-49b4-9f29-343008f1ec67',
                'measurement_id': 'f6e1142f-b510-40e9-8851-ea750e8e944b',
                'timestamp': 1728586719.9010828,
                'temperature': 25.53325080871582,
            },
            # New measurements
            {
                'experiment': '03113f5b-f19a-484b-a799-c3f5a0d432a5',
                'sensor': 'b007a37d-9626-4fb0-b970-8b3ac7d4ba5b',
                'measurement_id': 'a7c22f3d-6c91-4814-9f0d-7c0f1bb5c9b2',
                'timestamp': 1728586720.1010828,
                'temperature': 25.72893142700195,
            },
            {
                'experiment': '03113f5b-f19a-484b-a799-c3f5a0d432a5',
                'sensor': '3613db1c-e578-49b4-9f29-343008f1ec67',
                'measurement_id': 'a7c22f3d-6c91-4814-9f0d-7c0f1bb5c9b2',
                'timestamp': 1728586720.1010828,
                'temperature': 25.77106857299805,
            },
            {
                'experiment': '03113f5b-f19a-484b-a799-c3f5a0d432a5',
                'sensor': 'b007a37d-9626-4fb0-b970-8b3ac7d4ba5b',
                'measurement_id': 'b9e44f1a-8d23-4c5f-9e67-f2d1a8b7c3d0',
                'timestamp': 1728586720.3010828,
                'temperature': 25.91456794738770,
            },
            {
                'experiment': '03113f5b-f19a-484b-a799-c3f5a0d432a5',
                'sensor': '3613db1c-e578-49b4-9f29-343008f1ec67',
                'measurement_id': 'b9e44f1a-8d23-4c5f-9e67-f2d1a8b7c3d0',
                'timestamp': 1728586720.3010828,
                'temperature': 25.98543205261230,
            }
        ],
    }

    experiment_id = experiment_data['experiment_configured']['experiment']
    lower_threshold = experiment_data['experiment_configured']['temperature_range']['lower_threshold']
    upper_threshold = experiment_data['experiment_configured']['temperature_range']['upper_threshold']
    
    # Create a dictionary to store temperature values for each measurement_id
    temp_dict = {}

    # Iterate through the sensor measurements
    for measurement in experiment_data['sensor_temperature_measured']:
        measurement_id = measurement['measurement_id']
        temp = measurement['temperature']
        
        # Store temperatures in a dictionary by measurement_id
        if measurement_id not in temp_dict:
            temp_dict[measurement_id] = []
        temp_dict[measurement_id].append(measurement)

    # Calculate the average temperature for each measurement_id
    for measurement_id, measurements in temp_dict.items():
        # Compute the average temperature and take the most recent timestamp
        avg_temp = sum(m['temperature'] for m in measurements) / len(measurements)
        recent_timestamp = max(m['timestamp'] for m in measurements)  # Use the most recent timestamp

        # Prepare data to store in Redis
        data_to_store = {
            'experiment_id': experiment_id,
            'timestamp': recent_timestamp,
            'average_temperature': avg_temp,
            'lower_threshold': lower_threshold,
            'upper_threshold': upper_threshold,
            'measurement_id': measurement_id
        }
        
        # Store the data in Redis
        r.set(f"experiment_{experiment_id}_measurement_{measurement_id}", json.dumps(data_to_store))

        # Create an AverageMeasurements instance to store in the database
        avg_measurement = AverageMeasurements(
            exp_id=experiment_id,
            measurement_id=measurement_id,
            average_temperature=avg_temp,
            timestamp=data_to_store['timestamp'],  # Use the timestamp from data_to_store
            lower_threshold=lower_threshold,
            upper_threshold=upper_threshold,
            researcher_email=experiment_data['experiment_configured']['researcher']
        )
        db.add(avg_measurement)

    db.commit()  # Commit all changes to the database after all measurements have been processed






@app.get("/temperature")
def get_experiment_data(
    experiment_id: str,
    start_time: float,
    end_time: float,
    db: Session = Depends(get_db)):

    # Query the measurements
    measurements = db.query(AverageMeasurements).filter(
        AverageMeasurements.exp_id == experiment_id,
        AverageMeasurements.timestamp >= start_time,
        AverageMeasurements.timestamp <= end_time
    ).all()

    # Debugging output for SQLAlchemy
    print("Query Executed: ", str(db.query(AverageMeasurements).filter(
        AverageMeasurements.exp_id == experiment_id,
        AverageMeasurements.timestamp >= start_time,
        AverageMeasurements.timestamp <= end_time
    )))

    if measurements:
        print("Retrieved Measurements:")
        for measurement in measurements:
            print(measurement.__dict__)
    else:
        print("No measurements found.")

    # Check if measurements exist
    if not measurements:
        raise HTTPException(status_code=404, detail="No temperature measurements found for this interval.")

    # Prepare response data
    response_data = [
        {"timestamp": measurement.timestamp, "temperature": measurement.average_temperature}
        for measurement in measurements
    ]

    return response_data





