from fastapi import FastAPI
from routes import clients
import logging

app = FastAPI()
app.include_router(clients.router)

logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    logging.info("Root endpoint accessed")
    return {"message": "Welcome to the User Management API!"}