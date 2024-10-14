from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, Sequence
from sqlalchemy.orm import relationship
from database import Base



# class Measurements(Base):
#     __tablename__ = 'measurements'
    
#     id = Column(Integer, primary_key=True, index=True)
#     exp_id = Column(String, nullable=False)
#     measurement_id = Column(String, nullable=True)
#     sensor = Column(String, nullable=True)
#     timestamp = Column(Float, nullable=True)
#     temperature = Column(Float, nullable=True)
#     measurement_hash = Column(String, nullable=True)
#     lower_threshold = Column(Float, nullable=True)
#     upper_threshold = Column(Float, nullable=True)




class AverageMeasurements(Base):
    __tablename__ = 'average_measurements'
    
    id = Column(Integer, primary_key=True, index=True)
    exp_id = Column(String, nullable=False)  
    measurement_id = Column(String, nullable=True)  
    average_temperature = Column(Float, nullable=True)  
    timestamp = Column(Float, nullable=True)  
    lower_threshold = Column(Float, nullable=True)  
    upper_threshold = Column(Float, nullable=True)  
    researcher_email = Column(String, nullable=True)
    measurement_hash = Column(String, nullable=True)

