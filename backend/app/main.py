from fastapi import FastAPI

from app.database import Base, engine

# Import all models
from app.models import *

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Task & Knowledge Management API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Backend is running successfully."
    }