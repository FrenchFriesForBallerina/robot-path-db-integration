from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config

# initializing the SQLAlchemy engine
engine = create_engine(config.DATABASE_URL)

# creating session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# initialize the base for models
Base = declarative_base()

def initialize_db():
    print("Creating database and tables...")
    Base.metadata.create_all(engine)
    print("Tables created successfully.")