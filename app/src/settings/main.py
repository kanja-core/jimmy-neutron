# settings.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from .openai import OpenAi
from .llamaParse import LlamaParse


class Settings(OpenAi, LlamaParse, BaseSettings):
    model_config = SettingsConfigDict(
        # `.env.prod` takes priority over `.env`
        env_file=(".env", ".env.prod"),
        extra="allow",
    )


settings = Settings()

# # Usage example:
# if __name__ == "__main__":
#     seti = Settings()
#     print(seti.openai_api_base)
