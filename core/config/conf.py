from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import BaseModel

BASE_DIR = Path(__file__).parent.parent.parent
DB_PATH = BASE_DIR / "cyber_one.sqlite3"


class DBSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"


class Settings(BaseSettings):
    api_v1: str = "/api/v1"
    
    db_settings: DBSettings = DBSettings()
    

settings = Settings()