from fastapi import APIRouter
from .paths import router as paths_router
#todo: from .segments import router as segments_router

# initializing the main router
api_router = APIRouter()

# including individual routers
api_router.include_router(paths_router, prefix="/paths", tags=["paths"])
#todo: api_router.include_router(segments_router, prefix="/segments", tags=["segments"])