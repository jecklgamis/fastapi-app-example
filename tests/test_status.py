import base64

import pytest
from httpx import AsyncClient

from app.config import settings


def _basic_auth_header(username: str, password: str) -> dict[str, str]:
    credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
    return {"Authorization": f"Basic {credentials}"}


@pytest.mark.asyncio
async def test_status_with_valid_credentials(client: AsyncClient):
    headers = _basic_auth_header(settings.status_username, settings.status_password)
    response = await client.get("/status/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "app" in data
    assert "system" in data
    assert "resources" in data
    assert data["app"]["version"] == "0.1.0"
    assert data["app"]["uptime_seconds"] >= 0


@pytest.mark.asyncio
async def test_status_with_invalid_credentials(client: AsyncClient):
    headers = _basic_auth_header("admin", "wrong")
    response = await client.get("/status/", headers=headers)
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_status_without_credentials(client: AsyncClient):
    response = await client.get("/status/")
    assert response.status_code == 401
