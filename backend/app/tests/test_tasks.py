import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_and_read_tasks(client: AsyncClient):
    # Register + Login
    await client.post(
        "/auth/register",
        json={
            "username": "taskuser",
            "email": "task@example.com",
            "password": "secret",
        },
    )
    login = await client.post(
        "/auth/login", data={"username": "taskuser", "password": "secret"}
    )
    token = login.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}

    # Create task
    res = await client.post(
        "/tasks/",
        json={"title": "My First Task", "description": "Description"},
        headers=headers,
    )

    assert res.status_code == 200
    task = res.json()
    assert task["title"] == "My First Task"

    # Get tasks
    res = await client.get("/tasks/", headers=headers)
    tasks = res.json()
    assert len(tasks) == 1
