from datetime import datetime
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, Text
from utils.dal import BaseModel
from backend.models.enums import Sender


class MessageModel(BaseModel):

    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"), nullable=False)
    sender = Column(Enum(Sender), nullable=False)
    message_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "conversation_id": self.conversation_id,
            "sender": self.sender.value,
            "message_text": self.message_text,
            "created_at": str(self.created_at)
        }
