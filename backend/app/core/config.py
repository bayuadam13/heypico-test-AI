import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings  # ✅ ini versi baru

load_dotenv()

class Settings(BaseSettings):
    GOOGLE_MAPS_API_KEY: str = os.getenv("GOOGLE_MAPS_API_KEY", "")
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))
    USE_SAMPLE: bool = os.getenv("USE_SAMPLE", "false").lower() in ("1","true","yes")

settings = Settings()
