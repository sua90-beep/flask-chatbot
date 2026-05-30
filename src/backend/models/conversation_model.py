from datetime import datetime
from sqlalchemy import Column, DateTime, Integer
from utils.dal import BaseModel


class ConversationModel(BaseModel):

    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "created_at": str(self.created_at)
        }
