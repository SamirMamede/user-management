import pytest
import pytest_asyncio
import os
from app.database import get_collection
from app.exceptions import MongoDBConnectionError

@pytest.mark.asyncio
async def test_database_connection():
    coll = await get_collection()
    assert coll is not None
    assert coll.name == "Clientes"

@pytest.mark.asyncio
async def test_database_connection_failure():
    original_mongo_details = os.getenv("MONGO_DETAILS")
    os.environ["MONGO_DETAILS"] = "mongodb://invalid_host:27017"
    async with pytest_asyncio.assert_raises(MongoDBConnectionError):
        await get_collection()
    os.environ["MONGO_DETAILS"] = original_mongo_details