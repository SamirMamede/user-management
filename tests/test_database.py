import pytest
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from unittest.mock import AsyncMock
from app.database import get_collection, collection

@pytest.mark.asyncio
async def test_get_collection():
    """Verifica se a função get_collection retorna a coleção correta."""
    assert get_collection() == collection

@pytest.mark.asyncio
async def test_insert_document(monkeypatch):
    """Verifica se um documento pode ser inserido na coleção."""
    mock_insert_one = AsyncMock()
    monkeypatch.setattr(collection, "insert_one", mock_insert_one)

    new_document = {"name": "Teste", "age": 30}
    await get_collection().insert_one(new_document)
    mock_insert_one.assert_called_once_with(new_document)


@pytest.mark.asyncio
async def test_find_document(monkeypatch):
    """Verifica se um documento pode ser encontrado na coleção."""
    mock_find_one = AsyncMock(return_value={"name": "Teste", "age": 30})
    monkeypatch.setattr(collection, "find_one", mock_find_one)

    found_document = await get_collection().find_one({"name": "Teste"})
    assert found_document == {"name": "Teste", "age": 30}


@pytest.mark.asyncio
async def test_update_document(monkeypatch):
    """Verifica se um documento pode ser atualizado na coleção."""
    mock_update_one = AsyncMock(return_value= {"modifiedCount": 1})
    monkeypatch.setattr(collection, "update_one", mock_update_one)

    await get_collection().update_one({"name": "Teste"}, {"$set": {"age": 31}})
    mock_update_one.assert_called_once_with({"name": "Teste"}, {"$set": {"age": 31}})


@pytest.mark.asyncio
async def test_delete_document(monkeypatch):
    """Verifica se um documento pode ser excluído na coleção."""
    mock_delete_one = AsyncMock(return_value= {"deletedCount": 1})
    monkeypatch.setattr(collection, "delete_one", mock_delete_one)
    await get_collection().delete_one({"name": "Teste"})
    mock_delete_one.assert_called_once_with({"name": "Teste"})