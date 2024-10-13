from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, Sequence
from sqlalchemy.orm import relationship
from database import Base


from database import Base # Import Base from database.py

class Measurements(Base):
    __tablename__ = 'measurements'
    
    id = Column(Integer, primary_key=True, index=True)
    exp_id = Column(String, nullable=False)
    measurement_id = Column(String, nullable=True)
    sensor = Column(String, nullable=True)
    timestamp = Column(Float, nullable=True)
    temperature = Column(Float, nullable=True)
    measurement_hash = Column(String, nullable=True)
    lower_threshold = Column(Float, nullable=True)
    upper_threshold = Column(Float, nullable=True)




class AverageMeasurements(Base):
    __tablename__ = 'average_measurements'
    
    id = Column(Integer, primary_key=True, index=True)
    exp_id = Column(String, nullable=False)  # Assuming this relates to the experiment
    measurement_id = Column(String, nullable=True)  # Measurement ID to group by
    average_temperature = Column(Float, nullable=True)  # Average temperature
    timestamp = Column(Float, nullable=True)  # Timestamp of the measurement
    lower_threshold = Column(Float, nullable=True)  # Lower threshold
    upper_threshold = Column(Float, nullable=True)  # Upper threshold

