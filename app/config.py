import os
from enum import StrEnum

from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(StrEnum):
    DEV = "dev"
    TEST = "test"
    PROD = "prod"


APP_ENV = Environment(os.getenv("APP_ENV", Environment.DEV))

_env_files = {
    Environment.DEV: ".env.dev",
    Environment.TEST: ".env.test",
    Environment.PROD: ".env.prod",
}


class _BaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=_env_files[APP_ENV],
        env_file_encoding="utf-8",
    )

    app_env: Environment = APP_ENV
    app_name: str = "fastapi-app-template"
    debug: bool = False

    secret_key: str = "change-me-in-production"
    access_token_expire_minutes: int = 30

    status_username: str = "admin"
    status_password: str = "password"


class DevSettings(_BaseSettings):
    debug: bool = True


class TestSettings(_BaseSettings):
    debug: bool = True
    app_name: str = "fastapi-app-template (test)"
    secret_key: str = "test-secret-key"
    status_username: str = "test-admin"
    status_password: str = "test-password"


class ProdSettings(_BaseSettings):
    debug: bool = False


_settings_map: dict[Environment, type[_BaseSettings]] = {
    Environment.DEV: DevSettings,
    Environment.TEST: TestSettings,
    Environment.PROD: ProdSettings,
}

settings = _settings_map[APP_ENV]()
