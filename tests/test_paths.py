from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_paths():
    response = client.get("/paths/all")
    assert response.status_code == 200 # http response code is 200 OK
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
 
'''

def test_create_path():
    response = client.post("/paths", json={
        "name": "Test Path",
        "origin_lat": 0.0,
        "origin_lon": 0.0,
        "total_length": 100.0
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Test Path"


def test_get_path():
    response = client.get("/paths/1")
    assert response.status_code == 200
    assert response.json()["path_id"] == 1

def test_create_path():
    response = client.post("/paths", json={"name": "Test Path 0", "origin_lat": 0.0, "origin_lon": 0.0, "total_length": 100.0})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Path"

'''