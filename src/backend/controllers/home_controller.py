from flask import Blueprint, render_template, request, session, redirect
from backend.services.chat_service import ChatService
from backend.models.enums import Sender

home_blueprint = Blueprint("home_controller", __name__)


@home_blueprint.route("/")
@home_blueprint.route("/home")
def home():
    session.pop("conversation_id", None)
    return render_template("pages/home.html", active="home", messages=[])


@home_blueprint.get("/home/conversation")
def current_conversation():
    conversation_id = session.get("conversation_id")
    if not conversation_id:
        return redirect("/home")

    with ChatService() as service:
        messages = service.get_messages(conversation_id)

    return render_template("pages/home.html", active="home", messages=messages)


@home_blueprint.post("/home/send")
def send_message():
    user_text = request.form.get("message", "").strip()
    if not user_text:
        return redirect("/home")

    with ChatService() as service:
        if not session.get("conversation_id"):
            conversation_id = service.create_conversation()
            session["conversation_id"] = conversation_id

        conversation_id = session["conversation_id"]

        service.save_message(conversation_id, Sender.user, user_text)

        assistant_reply = service.send_to_openai(conversation_id)

        service.save_message(conversation_id, Sender.assistant, assistant_reply)

        return redirect("/home/conversation")


@home_blueprint.get("/home/send")
def refresh_after_send():
    session.pop("conversation_id", None)
    return redirect("/home")


@home_blueprint.route("/home/new")
def new_conversation():
    session.pop("conversation_id", None)
    return redirect("/home")
