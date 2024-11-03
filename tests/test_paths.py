from fastapi.testclient import TestClient
from app.main import app
import random

client = TestClient(app)

def test_get_paths():
    response = client.get("/paths")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    print("Response JSON:", response.json())  # JSON response for debugging

    assert isinstance(response.json(), list) # response type is list
    assert len(response.json()) > 0 # at least one path in database

    expected_keys = {"path_id", "name", "origin_lat", "origin_lon", "total_length"}
    for path in response.json():
        assert isinstance(path, dict)
        assert expected_keys.issubset(path.keys())

        # fields format ok   
        assert isinstance(path["path_id"], int)
        assert isinstance(path["name"], str)
        assert isinstance(path["origin_lat"], float)
        assert isinstance(path["origin_lon"], float)
        assert isinstance(path["total_length"], float)

def test_get_path():
    # first post so that there is a known path
    response = client.post("/paths", json={
        "name": "Sample Path",
        "origin_lat": random.uniform(58, 60),
        "origin_lon": random.uniform(58, 60),
        "total_length": round(random.uniform(10, 200), 3)
    })

    path_id = response.json()["path_id"]

    response = client.get(f"/paths/{path_id}")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.json()["path_id"] == path_id

def test_create_path():
    response = client.post("/paths", json={
        "name": "Test Path",
        "origin_lat": random.uniform(58, 60),
        "origin_lon": random.uniform(58, 60),
        "total_length": round(random.uniform(10, 200), 3)
    })
    print('created new path')
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    assert response.json()["name"] == "Test Path"

def test_update_path():
    create_response = client.post("/paths", json={
        "name": "Path to Update",
        "origin_lat": random.uniform(58, 60),
        "origin_lon": random.uniform(58, 60),
        "total_length": round(random.uniform(10, 200), 3)
    })
    path_id = create_response.json()["path_id"]

    response = client.put(f"/paths/{path_id}", json={
        "name": "Modified Path",
        "origin_lat": random.uniform(58, 60),
        "origin_lon": random.uniform(58, 60),
        "total_length": round(random.uniform(10, 200), 3)
    })
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.json()["name"] == "Modified Path", "The path name was not updated as expected."
 
def test_delete_path():
    create_response = client.post("/paths", json={
        "name": "Path to Delete",
        "origin_lat": random.uniform(58, 60),
        "origin_lon": random.uniform(58, 60),
        "total_length": round(random.uniform(10, 200), 3)
    })
    path_id = create_response.json()["path_id"]

    response = client.delete(f"/paths/{path_id}")
    print(f"Deleted path with id {path_id}.")
    assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}" 

    # verify the path doesn't exist anymore
    response = client.get(f"/paths/{path_id}")
    assert response.status_code == 404, f"Expected status code 404 for non-existent path, but got {response.status_code}"