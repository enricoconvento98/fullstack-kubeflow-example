from pydantic import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = "postgresql://mluser:mlpassword@postgres/mldb"
    CORS_ORIGINS: list = [
        "http://localhost:3000",
        "http://frontend:3000"
    ]
    
    class Config:
        env_file = ".env"

settings = Settings()