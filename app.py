import random
from db import initialize_db, get_session
from models import Path
# from utils import generate_er_diagram_png

# initializing db
try:
    initialize_db()
except Exception as e:
    print(f"An error occurred during database initialization: {e}")

# adding data
try:
    with get_session() as session:
        test_path = Path(name="Test Path 1", origin_lat=0.0, origin_lon=0.0, total_length=random.random()*100)
        session.add(test_path)
        print("Test path added successfully.")
except Exception as e:
    print(f"An error occurred while adding data: {e}")

# generate_er_diagram_png()