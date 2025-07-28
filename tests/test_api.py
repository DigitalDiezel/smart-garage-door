from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_predict_telemetry():
    response = client.post("/predict", json={
        "timestamp": "2024-07-08T17:35:20",
        "state": 1
    })
    assert response.status_code == 200
    assert "anomaly" in response.json()
