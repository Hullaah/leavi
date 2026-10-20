"""
Settings for the application.
"""

from typing import TYPE_CHECKING, TypedDict, Unpack

from pydantic import Field
from pydantic_settings import BaseSettings

if TYPE_CHECKING:
    from pathlib import Path


class SettingsKwarg(TypedDict, total=False):
    db_provider: str
    db_driver: str
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

    app_env: str
    debug: bool


class Settings(BaseSettings):
    """
    Settings for the application.
    """

    # database settings
    db_provider: str = "postgresql"
    db_driver: str = "psycopg"
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "eventhub"
    db_user: str = "hullaah"
    db_password: str

    # app settings
    environment: str = Field("development", validation_alias="APP_ENV")
    debug: bool = False

    def __init__(
        self, env_file: str | Path, /, **kwargs: Unpack[SettingsKwarg]
    ) -> None:
        super().__init__(
            _env_file=env_file,
            _env_file_encoding="utf-8",
            **kwargs,
        )
