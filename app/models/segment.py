from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base

class SegmentType(Base):
    __tablename__ = 'segment_types'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    segments = relationship('Segment', back_populates='segment_type')  # backreference to Segment
