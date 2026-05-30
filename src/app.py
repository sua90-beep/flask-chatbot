from flask import Flask
from backend.controllers.home_controller import home_blueprint
from backend.controllers.about_controller import about_blueprint
from backend.middleware.error_handler import register_exception_handlers
from utils.app_config import AppConfig

server = Flask(
	__name__,
	template_folder="Frontend/templates",
	static_folder="Frontend/static"
)

server.secret_key = AppConfig.server_side_session_secret_key

register_exception_handlers(server)

server.register_blueprint(home_blueprint)
server.register_blueprint(about_blueprint)


# Running in terminal:
# flask --app src/app.py run --debug

# Installations:
# pip install flask
# pip install python-dotenv
# pip install mysql-connector-python
# pip install sqlalchemy
# pip install pydantic
# pip install openai

# pip freeze > requirements.txt
