from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str = "development"
    APP_NAME: str = "Style Analysis AI"
    API_V1_PREFIX: str = "/api/v1"

    class Config:
        env_file = ".env"


settings = Settings()
