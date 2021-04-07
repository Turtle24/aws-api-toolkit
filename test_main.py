import pytest
from httpx import AsyncClient
from connections.redshift import RedShiftData

@pytest.mark.asyncio
async def test_redshiftdata():
    res = await RedShiftData().list_tables()
    assert list == type(res)