from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

from base import Base

class Path(Base):
    __tablename__ = 'paths'
    path_id = Column(Integer, primary_key=True)
    name = Column(String)
    origin_lat = Column(Float)
    origin_lon = Column(Float)
    total_length = Column(Float)

    segments = relationship('Segment', back_populates='path')

class Segment(Base):
    __tablename__ = 'segments'
    segment_id = Column(Integer, primary_key=True)
    path_id = Column(Integer, ForeignKey('paths.path_id'))
    segment_type_id = Column(Integer, ForeignKey('segment_types.segment_type_id'))
    start_lat = Column(Float)
    start_lon = Column(Float)
    end_lat = Column(Float)
    end_lon = Column(Float)
    curvature = Column(Float)
    segment_length = Column(Float)

    path = relationship('Path', back_populates='segments')
    performances = relationship('PerformanceData', back_populates='segment')
    segment_type = relationship('SegmentType')

class SegmentType(Base):
    __tablename__ = 'segment_types'
    segment_type_id = Column(Integer, primary_key=True)
    name = Column(String)

    segments = relationship('Segment', back_populates='segment_type')

class InputParameters(Base):
    __tablename__ = 'input_parameters'
    parameter_set_id = Column(Integer, primary_key=True)
    k_gain = Column(Float)
    speed = Column(Float)
    other_parameters = Column(String)

    performances = relationship('PerformanceData', back_populates='input_parameters')

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
