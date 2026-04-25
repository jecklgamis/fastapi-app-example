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
    app_name: str = "fastapi-app-example"
    debug: bool = False

    basic_auth_username: str = "admin"
    basic_auth_password: str = "password"


class DevSettings(_BaseSettings):
    debug: bool = True


class TestSettings(_BaseSettings):
    debug: bool = True
    app_name: str = "fastapi-app-example (test)"
    basic_auth_username: str = "test-admin"
    basic_auth_password: str = "test-password"


class ProdSettings(_BaseSettings):
    debug: bool = False


_settings_map: dict[Environment, type[_BaseSettings]] = {
    Environment.DEV: DevSettings,
    Environment.TEST: TestSettings,
    Environment.PROD: ProdSettings,
}

settings = _settings_map[APP_ENV]()
