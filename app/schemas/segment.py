from pydantic import BaseModel
from typing import Optional

# creating a new segment
class SegmentCreate(BaseModel):
    path_id: int
    segment_type_id: int
    start_lat: float
    start_lon: float
    end_lat: float
    end_lon: float
    curvature: float
    segment_length: float

# updating existing segment
class SegmentUpdate(BaseModel):
    segment_type_id: Optional[int] = None
    start_lat: Optional[float] = None
    start_lon: Optional[float] = None
    end_lat: Optional[float] = None
    end_lon: Optional[float] = None
    curvature: Optional[float] = None
    segment_length: Optional[float] = None

# reading segment data
class SegmentResponse(BaseModel):
    id: int
    path_id: int
    segment_type_id: int
    start_lat: float
    start_lon: float
    end_lat: float
    end_lon: float
    curvature: float
    segment_length: float

    class Config:
        orm_mode = True  # allows using ORM objects (like SQLAlchemy models) directly
