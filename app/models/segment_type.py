from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base

class SegmentType(Base):
    __tablename__ = 'segment_types'
    segment_type_id = Column(Integer, primary_key=True)
    name = Column(String)

    segments = relationship('Segment', back_populates='segment_type')
