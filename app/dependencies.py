# good to have for database sessions, auth checks, etc. plus caching 
from app.db import SessionLocal 

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

