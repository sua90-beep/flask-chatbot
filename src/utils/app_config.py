from dotenv import load_dotenv
from os import getenv

load_dotenv()

class AppConfig:

    connection_string: str = str(getenv("CONNECTION_STRING"))

    server_side_session_secret_key: str = str(getenv("SERVER_SIDE_SESSION_SECRET_KEY"))

    openai_api_key: str = str(getenv("OPENAI_API_KEY"))
