from fastapi import APIRouter
from app.api.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter()

chat_service = ChatService()

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    result = chat_service.get_answer(request.question)

    return result