from fastapi import FastAPI
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    logging.info("Root endpoint accessed")
    return {"message": "Welcome to the User Management API!"}