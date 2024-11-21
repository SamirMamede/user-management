def clientEntity(client) -> dict:
    return { 
        "id": str(client["_id"]),
        "name": client["name"],
    }