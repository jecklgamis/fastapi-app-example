import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_build_info(client: AsyncClient):
    response = await client.get("/build-info")
    assert response.status_code == 200
    data = response.json()
    assert "app" in data
    assert "version" in data
    assert "git_commit" in data
    assert "git_branch" in data
    assert "build_timestamp" in data
