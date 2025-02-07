from pydantic import SecretStr


class Escavador:
    escavador_api_key: SecretStr
    escavador_api_base: str
    escavador_webhook_url: str | None = None
