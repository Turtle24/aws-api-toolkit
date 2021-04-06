import pytest
from httpx import AsyncClient

from main import app
from database import get_db

@pytest.mark.asyncio
async def test_home():
    async with AsyncClient(app=app, base_url='http://127.0.0.1:8000') as ac:
        response = await ac.get("/home")
    assert response.status_code == 200
    assert response.json() == {'data': 'Home'}

@pytest.mark.asyncio
async def test_get_counties():
    async with AsyncClient(app=app, base_url='http://127.0.0.1:8000/home') as ac:
        response = await ac.get("/counties")
    assert response.status_code == 200
    assert response.json()[0] == {
                        "date": "2020-01-21",
                        "county": "Snohomish",
                        "state": "Washington",
                        "fips": 53061,
                        'cases': 1,
                        'deaths': 0
                        }