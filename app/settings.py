"""
Application settings handled using Pydantic Settings management.

Pydantic is used both to read app settings from various sources, and to validate their
values.

https://docs.pydantic.dev/latest/usage/settings/
"""
from pydantic import BaseModel
from pydantic_settings import BaseSettings


class APIInfo(BaseModel):
    title = "blacksheep-chat API"
    version = "0.0.1"


class App(BaseModel):
    show_error_details = False


class Site(BaseModel):
    copyright: str = "For anybody to find"


class Settings(BaseSettings):

    info: APIInfo = APIInfo()

    app: App = App()

    class Config:
        env_prefix = "APP_"


def load_settings() -> Settings:
    return Settings()
