from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base

class InputParameters(Base):
    __tablename__ = 'input_parameters'
    parameter_set_id = Column(Integer, primary_key=True)
    k_gain = Column(Float)
    speed = Column(Float)
    other_parameters = Column(String)

    performances = relationship('PerformanceData', back_populates='input_parameters')
