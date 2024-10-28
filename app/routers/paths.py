# purpose: define endpoints for paths

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db_session
from app.models.path import Path
from app.schemas import PathSchema
from typing import List  

router = APIRouter()

# base endpoint for the paths router
@router.get("/")
async def main():
    return {"message": "Hello from the main paths router!"}

@router.get("/all", response_model=List[PathSchema], tags=["paths"])
async def get_paths(db: Session=Depends(get_db_session)): # this is dependency injection case!
    paths = db.query(Path).all()
    if paths is None:
        raise HTTPException(status_code=404, detail="Paths not found")
    #return [PathSchema.from_orm(path).dict() for path in paths]
    return paths
'''
todo: 
@router.post("/paths")
async def create_path(path: Path, db: Session = Depends(get_db_session)):
    db_path = Path(
        name=path.name,
        origin_lat=path.origin_lat,
        origin_lon=path.origin_lon,
        total_length=path.total_length,
    )
    db.add(db_path)
    db.commit()
    db.refresh(db_path)
    return db_path
'''