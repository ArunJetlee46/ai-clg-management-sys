from fastapi.testclient import TestClient
from app.main import app


def test_load_smoke():
    client = TestClient(app)
    for _ in range(10):
        assert client.get('/health').status_code == 200
