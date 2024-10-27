'''
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db_session
from app.schemas.path import SegmentCreate, PathResponse
from app.models import Segment as SegmentModel

router = APIRouter()

todo: router get, post
'''