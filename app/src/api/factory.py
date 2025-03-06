from pydantic import SecretStr

from .mock.main import MockAPI
from .main import API
from .protocol import APIProtocol
from ..settings.main import settings


class APIFactory:
    @staticmethod
    def get(
        base_url: str,
        api_key: SecretStr | None = None,
        extra_headers: dict | None = None,
        extra_params: dict | None = None,
    ) -> API:
        return API(
            base_url=base_url,
            api_key=api_key,
            extra_headers=extra_headers,
            extra_params=extra_params,
        )

    @staticmethod
    def bot() -> APIProtocol:
        return API(
            settings.bot_api_base,
            # settings.bot_api_key,
        )

    @staticmethod
    def escavador() -> APIProtocol:
        return API(
            settings.escavador_api_base,
            settings.escavador_api_key,
            extra_headers={
                "X-Requested-With": "XMLHttpRequest",
                "Accept": "application/json",
            },
        )

    @staticmethod
    def escavador_mock() -> APIProtocol:
        return MockAPI(
            settings.escavador_api_base, log_file="app/src/api/mock/lawsuits.json"
        )
