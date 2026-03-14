from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    app_name: str = "FastAPI App"
    debug: bool = False

    secret_key: str = "change-me-in-production"
    access_token_expire_minutes: int = 30

    status_username: str = "admin"
    status_password: str = "password"


settings = Settings()
