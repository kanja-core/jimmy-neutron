import json
from ..protocol import APIProtocol
from pydantic import SecretStr
from typing import Type
from ..types import T


class MockAPI(APIProtocol):
    def __init__(
        self,
        base_url: str,
        api_key: SecretStr | None = None,
        extra_headers: dict | None = None,
        extra_params: dict | None = None,
        log_file: str = "log.txt",
    ):
        """
        Mock API that reads responses from a log file containing a single JSON entry.

        :param log_file: Path to the log file containing API response.
        """
        self.base_url = base_url
        self.log_file = log_file
        self.headers = {
            "Content-Type": "application/json",
        }

        if api_key:
            self.headers["Authorization"] = f"Bearer {api_key.get_secret_value()}"

        if extra_headers:
            self.headers.update(extra_headers)

        self.default_params = extra_params or {}

    def request(
        self,
        method: str,
        endpoint: str,
        response_type: Type[T],
        params: dict | None = None,
        data: dict | None = None,
    ) -> T:
        """Simulates an API request by reading the mock response from the log file.

        :param method: HTTP method (GET, POST, etc.)
        :param endpoint: API endpoint (used as key in mock data)
        :param params: Query parameters (unused)
        :param data: Request body data (unused)
        :param response_type: Expected response type (e.g., dict or Pydantic model)
        :return: Mock API response as a dictionary or a dataclass/Pydantic object.
        """

        key = f"{method.upper()} {endpoint}"  # Example: "GET /users"

        mock_data = json.load(open(self.log_file, "r"))

        print(mock_data)

        if self.base_url not in mock_data:
            raise ValueError(f"Base URL '{self.base_url}' not found in log data")

        if key not in mock_data[self.base_url]:
            raise ValueError(
                f"Mock response for '{key}' not found for base URL '{self.base_url}'"
            )

        json_response = json.dumps(
            mock_data[self.base_url][key]["response"]["body"], ensure_ascii=False
        )

        return response_type.model_validate_json(json_response)

    def get(
        self,
        endpoint: str,
        response_type: Type[T],
        params: dict | None = None,
    ) -> T:
        return self.request("GET", endpoint, params=params, response_type=response_type)

    def post(
        self,
        endpoint: str,
        response_type: Type[T],
        data: dict | None = None,
    ) -> T:
        return self.request("POST", endpoint, data=data, response_type=response_type)

    def put(
        self,
        endpoint: str,
        response_type: Type[T],
        data: dict | None = None,
    ) -> T:
        return self.request("PUT", endpoint, data=data, response_type=response_type)

    def delete(self, endpoint: str, response_type: Type[T]) -> T:
        return self.request("DELETE", endpoint, response_type=response_type)
