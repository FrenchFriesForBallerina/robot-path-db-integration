from pydantic import BaseModel # pydantic is great for validating data from API requests and formatting responses
from typing import Optional

# creating new path
class PathCreate(BaseModel):
    name: str
    origin_lat: float
    origin_lon: float
    total_length: float

# updating an existing path
class PathUpdate(BaseModel):
    name: Optional[str] = None
    origin_lat: Optional[float] = None
    origin_lon: Optional[float] = None
    total_length: Optional[float] = None

# reading path data
class PathResponse(BaseModel):
    path_id: int
    name: str
    origin_lat: float
    origin_lon: float
    total_length: float

    class Config:
        orm_mode = True  # allows using ORM objects (like SQLAlchemy models) directly
