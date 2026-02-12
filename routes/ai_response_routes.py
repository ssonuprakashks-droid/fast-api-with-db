from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import get_db
from utils.ai_response import get_completion
from schemas.ai_response_schemas import AIRequest, AIResponse
from schemas.chat_schemas import ChatHistoryResponse
from utils.auth import get_current_user
from models import User
from repositories.chat_repo import ChatRepo

router = APIRouter()


@router.post("/ask", response_model=AIResponse)
def ask_ai(request: AIRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Get response from AI model and save to history."""
    try:
        chat_repo = ChatRepo(db)
        
        # Save user message
        chat_repo.add_message(user_id=current_user.id, role="user", content=request.message)
        
        # Get AI response
        response = get_completion(request.message, request.system_prompt)
        
        # Save AI response
        chat_repo.add_message(user_id=current_user.id, role="assistant", content=response)
        
        return AIResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history", response_model=ChatHistoryResponse)
def get_history(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Retrieve chat history for the authenticated user."""
    chat_repo = ChatRepo(db)
    messages = chat_repo.get_user_messages(current_user.id)
    return ChatHistoryResponse(messages=messages)