from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

import config
from models import Base

# initializing the engine
engine = create_engine(config.DATABASE_URL)

# Create all tables defined by models
def initialize_db():
    print("Creating database and tables...")
    Base.metadata.create_all(engine)
    print("Tables created successfully.")

# session factory
Session = sessionmaker(bind=engine)

# context manager for sessions
# a new manager created each time getsession is called
@contextmanager
def get_session():
    session = Session()
    try:
        yield session # session is yielded to allow interaction w/the db
        session.commit()  # commit transaction if all is well
    except Exception as e:
        session.rollback()  # rollback transaction on error
        print(f"An error occurred: {e}")
        raise  # re-raise the exception after rollback for logging or further handling
    finally:
        session.close()  # closing the session