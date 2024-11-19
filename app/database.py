from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb://admin:123@localhost:27017"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.user_management
collection = database.Clientes

def get_collection():
    return collection