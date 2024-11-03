# purpose: define endpoints for paths

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies import get_db_session
from app.models.path import Path
from app.schemas import PathSchema
from typing import List

from app.schemas.path import PathCreate, PathUpdate  

router = APIRouter()

# get all paths
@router.get("/", response_model=List[PathSchema], status_code=status.HTTP_200_OK, tags=["paths"])
async def get_paths(db: Session=Depends(get_db_session)): # this is dependency injection case!
    paths = db.query(Path).all()
    return paths # empty list if no paths

# get a specific path by id
@router.get("/{path_id}", response_model=PathSchema, status_code=status.HTTP_200_OK, tags=["paths"])
async def get_path(path_id: int, db: Session=Depends(get_db_session)): # this is dependency injection case!
    path = db.query(Path).filter(Path.path_id == path_id).first()
    if not path:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Path not found")
    return path

# create a new path
@router.post("/", response_model=PathSchema, status_code=status.HTTP_201_CREATED, tags=["paths"])
async def create_path(path: PathCreate, db: Session = Depends(get_db_session)):
    db_path = Path(**path.dict())
    db.add(db_path)
    db.commit()
    db.refresh(db_path)
    return db_path

# update a path
@router.put("/{path_id}", response_model=PathSchema, status_code=status.HTTP_200_OK, tags=["paths"])
async def update_path(path_id: int, path: PathUpdate, db: Session = Depends(get_db_session)):
    # get existing path from the database
    db_path = db.query(Path).filter(Path.path_id == path_id).first()
    if not db_path:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Path not found")
    
    # update the path's fields
    for key, value in path.dict(exclude_unset=True).items():
        setattr(db_path, key, value)

    db.commit()
    db.refresh(db_path)
    return db_path

# delete a path by id
@router.delete("/{path_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["paths"])
async def delete_path(path_id: int, db: Session = Depends(get_db_session)):
    # find the path by the id
    db_path = db.query(Path).filter(Path.path_id == path_id).first()
    if not db_path:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Path not found")
    # delete the path
    db.delete(db_path)
    db.commit()
    return 