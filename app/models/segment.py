from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.db import Base

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

Segment.path = relationship('Path', back_populates='segments')
Segment.performances = relationship('PerformanceData', back_populates='segment')
Segment.segment_type = relationship('SegmentType')