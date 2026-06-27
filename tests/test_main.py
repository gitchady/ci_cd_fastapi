from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_returns_message() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI CI/CD demo"}


def test_health_check_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_read_item_returns_item() -> None:
    response = client.get("/items/42")

    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "name": "Item 42"}
