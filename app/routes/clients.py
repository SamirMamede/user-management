from fastapi import APIRouter

router = APIRouter()

@router.get("/clients")
def get_clients():
    return "Hello World"

@router.post("/clients")
def create_client():
    return "Hello World"

@router.put("/clients/{client_id}")
def update_client(client_id: int):
    return "Hello World"

@router.delete("/clients/{client_id}")
def delete_client(client_id: int):
    return "Hello World"