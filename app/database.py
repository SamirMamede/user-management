import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure, CollectionInvalid
from app.exceptions import MongoDBConnectionError, MongoDBCollectionError

load_dotenv()
MONGO_DETAILS = os.getenv("MONGO_DETAILS")

async def get_collection():
    try:
        client = AsyncIOMotorClient(MONGO_DETAILS)
        await client.server_info()
        database = client.user_management
        collection = database.Clientes
        return collection
    except ConnectionFailure as e:
        raise MongoDBConnectionError(f"Erro de conexão com o MongoDB: {e}") from e
    except CollectionInvalid as e:
        raise MongoDBCollectionError(f"Coleção 'Clientes' não encontrada: {e}") from e
    except Exception as e:
        raise