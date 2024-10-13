from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import Measurements, AverageMeasurements
import models
from database import engine, SessionLocal
from sqlalchemy import func

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
    "stabilization_started": {
        'experiment': '03113f5b-f19a-484b-a799-c3f5a0d432a5',
        'timestamp': 1728586719.1191473
    },
    "experiment_started": {
        'experiment': '03113f5b-f19a-484b-a799-c3f5a0d432a5',
        'timestamp': 1728586719.9999887
    },
    "sensor_temperature_measured": [
        {
            'experiment': '03113f5b-f19a-484b-a799-c3f5a0d432a5',
            'sensor': 'b007a37d-9626-4fb0-b970-8b3ac7d4ba5b',
            'measurement_id': 'e2e61ab8-4689-4c5f-9266-38a4201789c8',
            'timestamp': 1728586719.3376231,
            'temperature': 20.01945686340332,
            'measurement_hash': 'WtwTT8Kj/tfnRCe6.YOi2imtd4s9BfxpMrjsoFP/NmKCmDxCzBm789jUGlN4jQKexNy9ngdmVxci4Bcb1BGN9poHOpPvLwP141xDLaN0Ag+ojgFVgeV3ViRNf7b3LYt6cIVXgRRqZ5TeUg5F0ieXU8cbTj6u4K+c6lPFFhaMWTIyCKn1rcDcsmb+6Vz4GQYpIqj+7pTxHapOyz3L46f+KbXf5ou2PDtHhuyDMOafHOAfgHPxrgQsEBLsnSb1z8d02WqNdCuTJgQxKpWJTssqVCsvuVMvZu04IAo/NdP9e51Gu3A'
        },
        {
            'experiment': '03113f5b-f19a-484b-a799-c3f5a0d432a5',
            'sensor': '3613db1c-e578-49b4-9f29-343008f1ec67',
            'measurement_id': 'e2e61ab8-4689-4c5f-9266-38a4201789c8',
            'timestamp': 1728586719.3376231,
            'temperature': 21.98054313659668,
            'measurement_hash': 'WtwTT8Kj/tfnRCe6.YOi2imtd4s9BfxpMrjsoFP/NmKCmDxCzBm789jUGlN4jQKexNy9ngdmVxci4Bcb1BGN9poHOpPvLwP141xDLaN0Ag+ojgFVgeV3ViRNf7b3LYt6cIVXgRRqZ5TeUg5F0ieXU8cbTj6u4K+c6lPFFhaMWTIyCKn1rcDcsmb+6Vz4GQYpIqj+7pTxHapOyz3L46f+KbXf5ou2PDtHhuyDMOafHOAfgHPxrgQsEBLsnSb1z8d02WqNdCuTJgQxKpWJTssqVCsvuVMvZu04IAo/NdP9e51Gu3A'
        },
        {
            'experiment': '03113f5b-f19a-484b-a799-c3f5a0d432a5',
            'sensor': 'b007a37d-9626-4fb0-b970-8b3ac7d4ba5b',
            'measurement_id': 'dc111d44-54e2-41a2-a4ce-3c23345671c8',
            'timestamp': 1728586719.510183,
            'temperature': 26.05428123474121,
            'measurement_hash': 'QDVf3phA1kPllZQT.s6zsV+zDOOF+Aul9/q+Vudgda5VTdxIUSHbpFN09R4ENrvCV/V+RICSoIfPk4TtIMHxj7WZeq3CCAvmrOF6kLT8bEbw5Ab1vLcQ9XCLkfx7CTkIA47RkO6Y6M2rNW9FYCDNdg/GXR+u4mfsY6TgnOK4i/qYfXqLLdNvn5bNTb7dt0B9wP8lPoOxlgKVeDrCx7MWqhxRUsP19AD7PfLrXt+TBSKYkDWrLfufWiG+0MA25lI9Qfy7g2Inl2Tr7qBXMiqT909Cho22E3Ydy7OXYI3BU9D9xbaIrS4yv3wI'
        },
        {
            'experiment': '03113f5b-f19a-484b-a799-c3f5a0d432a5',
            'sensor': '3613db1c-e578-49b4-9f29-343008f1ec67',
            'measurement_id': 'dc111d44-54e2-41a2-a4ce-3c23345671c8',
            'timestamp': 1728586719.510183,
            'temperature': 25.94571876525879,
            'measurement_hash': 'QDVf3phA1kPllZQT.s6zsV+zDOOF+Aul9/q+Vudgda5VTdxIUSHbpFN09R4ENrvCV/V+RICSoIfPk4TtIMHxj7WZeq3CCAvmrOF6kLT8bEbw5Ab1vLcQ9XCLkfx7CTkIA47RkO6Y6M2rNW9FYCDNdg/GXR+u4mfsY6TgnOK4i/qYfXqLLdNvn5bNTb7dt0B9wP8lPoOxlgKVeDrCx7MWqhxRUsP19AD7PfLrXt+TBSKYkDWrLfufWiG+0MA25lI9Qfy7g2Inl2Tr7qBXMiqT909Cho22E3Ydy7OXYI3BU9D9xbaIrS4yv3wI'
        },
        {
            'experiment': '03113f5b-f19a-484b-a799-c3f5a0d432a5',
            'sensor': 'b007a37d-9626-4fb0-b970-8b3ac7d4ba5b',
            'measurement_id': 'f6e1142f-b510-40e9-8851-ea750e8e944b',
            'timestamp': 1728586719.9010828,
            'temperature': 25.46674919128418,
            'measurement_hash': 'xv33foNXWJ351Wpr.MhFJhljsM9uCv+pW4mzTuggrxYzPP1TWLHUcOwLHiZwTsDTovZ+2YiRyjB48hBDTO+/WDT3mFlHEUuWHzLMUaJpXfo56ckBPcUn/36hVreVS98o8fvcTWNQKLea2J2K28yR/teFJiE7tBklYU5+SD2PcisDEXeqwnZwVuUGh/UAC1ItQm07USDi5YARZNqgcPHpWjmzjFeTFE7g/1fwWUC99kADVRa/rXy6uhnHl8GTkqN5cchCmZZ9e0qpTrVXKKaX0zy9XimyoRZEoNTWzlyelvhxK+g/HyKXdHJd0'
        },
        {
            'experiment': '03113f5b-f19a-484b-a799-c3f5a0d432a5',
            'sensor': '3613db1c-e578-49b4-9f29-343008f1ec67',
            'measurement_id': 'f6e1142f-b510-40e9-8851-ea750e8e944b',
            'timestamp': 1728586719.9010828,
            'temperature': 25.53325080871582,
            'measurement_hash': 'xv33foNXWJ351Wpr.MhFJhljsM9uCv+pW4mzTuggrxYzPP1TWLHUcOwLHiZwTsDTovZ+2YiRyjB48hBDTO+/WDT3mFlHEUuWHzLMUaJpXfo56ckBPcUn/36hVreVS98o8fvcTWNQKLea2J2K28yR/teFJiE7tBklYU5+SD2PcisDEXeqwnZwVuUGh/UAC1ItQm07USDi5YARZNqgcPHpWjmzjFeTFE7g/1fwWUC99kADVRa/rXy6uhnHl8GTkqN5cchCmZZ9e0qpTrVXKKaX0zy9XimyoRZEoNTWzlyelvhxK+g/HyKXdHJd0'
        }
    ],
    "experiment_terminated": {
        'experiment': '03113f5b-f19a-484b-a799-c3f5a0d432a5',
        'timestamp': 1728586720.000001
    }
}


    try:
        # Save experiment data to the database based on stage
        for stage, data in experiment_data.items():
            if stage == 'experiment_configured':
                # Insert data from experiment_configured
                measurement_configured = models.Measurements(
                    exp_id=data['experiment'],
                    measurement_id=None,
                    sensor=None,
                    timestamp=None,
                    temperature=None,
                    measurement_hash=None,
                    lower_threshold=data['temperature_range']['lower_threshold'],
                    upper_threshold=data['temperature_range']['upper_threshold']
                )
                db.add(measurement_configured)

            elif stage == 'stabilization_started':
                # Insert data from stabilization_started
                stabilization_started = models.Measurements(
                    exp_id=data['experiment'],
                    measurement_id=None,
                    sensor=None,
                    timestamp=data['timestamp'],
                    temperature=None,
                    measurement_hash=None,
                    lower_threshold=None,
                    upper_threshold=None
                )
                db.add(stabilization_started)

            elif stage == 'experiment_started':
                # Insert data from experiment_started
                experiment_started = models.Measurements(
                    exp_id=data['experiment'],
                    measurement_id=None,
                    sensor=None,
                    timestamp=data['timestamp'],
                    temperature=None,
                    measurement_hash=None,
                    lower_threshold=None,
                    upper_threshold=None
                )
                db.add(experiment_started)

            elif stage == 'sensor_temperature_measured':
                # Insert each sensor's temperature measurement
                for measurement in data:
                    sensor_measurement = models.Measurements(
                        exp_id=measurement['experiment'],
                        measurement_id=measurement['measurement_id'],
                        sensor=measurement['sensor'],
                        timestamp=measurement['timestamp'],
                        temperature=measurement['temperature'],
                        measurement_hash=measurement['measurement_hash'],
                        lower_threshold=None,
                        upper_threshold=None
                    )
                    db.add(sensor_measurement)

            elif stage == 'experiment_terminated':
                # Insert data from experiment_terminated
                experiment_terminated = models.Measurements(
                    exp_id=data['experiment'],
                    measurement_id=None,
                    sensor=None,
                    timestamp=data['timestamp'],
                    temperature=None,
                    measurement_hash=None,
                    lower_threshold=None,
                    upper_threshold=None
                )
                db.add(experiment_terminated)

        db.commit()

        # Query to calculate average temperature for each measurement_id
        average_temperatures = (
        db.query(
            Measurements.exp_id,  # Include exp_id from Measurements
            Measurements.measurement_id,
            func.avg(Measurements.temperature).label('average_temperature'),  # Average temperature
            Measurements.timestamp,  # Just take the timestamp (since they are the same)
            Measurements.lower_threshold,  # Just take the lower threshold (since they are the same)
            Measurements.upper_threshold   # Just take the upper threshold (since they are the same)
        )
        .group_by(Measurements.exp_id, Measurements.measurement_id, Measurements.timestamp, Measurements.lower_threshold, Measurements.upper_threshold)  # Group by relevant fields
        .all())


        # Insert the calculated averages into the AverageMeasurements table
        for exp_id, measurement_id, average_temperature, timestamp, lower_threshold, upper_threshold in average_temperatures:
            average_measurement = AverageMeasurements(
                exp_id=exp_id,
                measurement_id=measurement_id,
                average_temperature=average_temperature,
                timestamp=timestamp,
                lower_threshold=lower_threshold,  
                upper_threshold=upper_threshold   
            )
            db.add(average_measurement)

        db.commit()

    except Exception as e:
        db.rollback()  # Rollback the transaction in case of error
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

    return {"message": "Experiment data populated and averages calculated successfully."}
