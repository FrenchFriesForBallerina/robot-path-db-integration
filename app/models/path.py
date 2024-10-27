from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.db import Base

class Path(Base):
    __tablename__ = 'paths'

    path_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    origin_lat = Column(Float)
    origin_lon = Column(Float)
    total_length = Column(Float)

    # todo: segments = relationship('Segment', back_populates='path')  # relationship to segments
