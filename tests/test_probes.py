import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_liveness(client: AsyncClient):
    response = await client.get("/probe/live")
    assert response.status_code == 200
    assert response.json() == {"status": "I'm alive!"}


@pytest.mark.asyncio
async def test_readiness(client: AsyncClient):
    response = await client.get("/probe/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "I'm ready!"}


@pytest.mark.asyncio
async def test_startup(client: AsyncClient):
    response = await client.get("/probe/startup")
    assert response.status_code == 200
    assert response.json() == {"status": "started"}
