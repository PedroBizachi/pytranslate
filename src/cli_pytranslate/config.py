from deep_translator import GoogleTranslator  # pyright: ignore[reportMissingTypeStubs]
from deep_translator.base import (  # pyright: ignore[reportMissingTypeStubs]
    BaseTranslator,
)
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    DEEPL_API: str = Field(default="provide_API_key")
    DEFAULT_TRANSLATOR: BaseTranslator = GoogleTranslator()
    DEFAULT_SOURCE: str = "auto"
    DEFAULT_TARGET: str = "en"


# Initialize once to share across the application
settings = Settings()
translator = settings.DEFAULT_TRANSLATOR
