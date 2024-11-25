from fastapi import APIRouter
from db import conn
from schemas import clientEntity, clientsEntity
client = APIRouter()

@client.get("/clients")
def find_all_client():
    return clientsEntity(conn.local.client.find())

@client.post("/clients")
def create_client():
    return "Hello World"

@client.get("/clients/{id}")
def find_client():
    return "Hello World"

@client.put("/clients/{id}")
def update_client():
    return "Hello World"

@client.delete("/clients/{id}")
def delete_client():
    return "Hello World"