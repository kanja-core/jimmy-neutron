from pydantic import SecretStr

class LlamaParse():
    llamaparse_api_key: SecretStr
    llamaparse_api_base: str
    llamaparse_webhook_url: str | None = None

    # class Config:
    #     env_file = ".env"  # Loads environment variables from a .env file if present