
import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app) # TestClient will raise an exception if response isn't valid json

def test_main():
    response = client.get("/")
    print("Response JSON:", response.json())  # JSON response for debugging

    assert response.status_code == 200
