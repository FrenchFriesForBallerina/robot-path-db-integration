from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db_session
from app.models.path import Path

router = APIRouter()

@router.get("/", tags=["paths"])
async def get_paths(db: Session=Depends(get_db_session)): # this is dependency injection case!
    paths = db.query(Path).all()
    return {"paths": paths}

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