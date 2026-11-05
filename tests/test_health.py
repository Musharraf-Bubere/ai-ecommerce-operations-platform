from fastapi.testclient import TestClient

from ecommerce_ops.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_unknown_route():
    response = client.get("/unknown")

    assert response.status_code == 404
