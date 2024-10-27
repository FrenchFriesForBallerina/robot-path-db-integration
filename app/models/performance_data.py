from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.db import Base

class PerformanceData(Base):
    __tablename__ = 'performance_data'
    performance_id = Column(Integer, primary_key=True)
    segment_id = Column(Integer, ForeignKey('segments.segment_id'))
    parameter_set_id = Column(Integer, ForeignKey('input_parameters.parameter_set_id'))
    time_taken = Column(Float)
    error = Column(Float)
    energy_consumption = Column(Float)

    segment = relationship('Segment', back_populates='performances')
    input_parameters = relationship('InputParameters', back_populates='performances')
