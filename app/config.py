from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load .env so Pydantic AI can read GOOGLE_API_KEY.
load_dotenv()


class Settings(BaseSettings):
    google_client_id: str
    google_client_secret: str
    google_refresh_token: str
    database_url: str
    classifier_model: str = "google:gemini-3.5-flash-lite"
    agent_model: str = "google:gemini-4-argon"
    poll_interval_seconds: int = 60
    dashboard_username: str = "admin"
    dashboard_password: str = ""


settings = Settings()
