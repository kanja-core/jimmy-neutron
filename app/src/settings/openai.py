from pydantic import SecretStr

class OpenAi():
    openai_api_key: SecretStr
    openai_api_base: str
    openai_model: str = "gpt-4o-mini"

    # class Config:
    #     env_file = ".env"  # Loads environment variables from a .env file if present