from typing import cast

from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from backend.models.conversation_model import ConversationModel
from backend.models.message_model import MessageModel
from backend.models.enums import Sender
from utils.dal import Dal
from utils.app_config import AppConfig


class ChatService:

    def __init__(self) -> None:
        self.dal = Dal()
        self.session = self.dal.create_session()
        self.client = OpenAI(api_key=AppConfig.openai_api_key)

    def create_conversation(self) -> int:
        conversation = ConversationModel()
        self.session.add(conversation)
        self.session.commit()
        return cast(int, conversation.id)

    def save_message(self, conversation_id: int, sender: Sender, text: str) -> MessageModel:
        message = MessageModel(
            conversation_id=conversation_id,
            sender=sender,
            message_text=text
        )
        self.session.add(message)
        self.session.commit()
        return message

    def get_messages(self, conversation_id: int) -> list[MessageModel]:
        messages = (
            self.session.query(MessageModel)
            .filter(MessageModel.conversation_id == conversation_id)
            .order_by(MessageModel.created_at)
            .all()
        )
        return messages

    def send_to_openai(self, conversation_id: int) -> str:
        messages = self.get_messages(conversation_id)
        openai_messages: list[ChatCompletionMessageParam] = [
            cast(ChatCompletionMessageParam, {"role": msg.sender.value, "content": msg.message_text})
            for msg in messages
        ]
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=openai_messages
        )
        return response.choices[0].message.content or ""

    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
