import pytest
from app.routes import clients
from fastapi.testclient import TestClient

client = TestClient(clients.router)

@pytest.mark.asyncio
async def test_get_clients():
    response = client.get("/clients")
    assert response.status_code == 200
    assert response.json() == "Hello World"