from sqlalchemy.orm import Session
from models import ChatMessage
from typing import List

class ChatRepo:
    def __init__(self, db: Session):
        self.db = db

    def add_message(self, user_id: int, role: str, content: str):
        db_message = ChatMessage(user_id=user_id, role=role, content=content)
        self.db.add(db_message)
        self.db.commit()
        self.db.refresh(db_message)
        return db_message

    def get_user_messages(self, user_id: int) -> List[ChatMessage]:
        return self.db.query(ChatMessage).filter(ChatMessage.user_id == user_id).order_by(ChatMessage.timestamp.asc()).all()
