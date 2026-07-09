from fastapi import APIRouter, Depends

from app.schemas.chat import ChatRequest
from app.services.chat_service import ask_ai
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"]
)


@router.post("/")
def chat(
    request: ChatRequest,
    current_user: User = Depends(get_current_user)
):
    return ask_ai(request.question)