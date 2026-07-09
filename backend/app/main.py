from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import Base, engine, SessionLocal
from app.models import *

from app.utils.seed import seed_roles

from app.routers.auth import router as auth_router
from app.routers.user import router as user_router
from app.routers.document import router as document_router
from app.routers.task import router as task_router
from app.routers.chat import router as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    seed_roles(db)
    db.close()

    yield


app = FastAPI(
    title="AI Task API",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(document_router)
app.include_router(task_router)
app.include_router(chat_router)

@app.get("/")
def home():
    return {
        "message": "Backend Running"
    }