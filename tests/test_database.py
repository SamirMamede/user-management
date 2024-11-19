import pytest
from app.database import get_collection

@pytest.mark.asyncio
async def test_database_connection():
    coll = get_collection()
    assert coll is not None
    assert coll.name == "Clientes"