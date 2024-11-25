from fastapi import FastAPI
from routes import client

app = FastAPI()
app.include_router(client)