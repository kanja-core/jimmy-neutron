from .protocol import APIProtocol
from pydantic import SecretStr
from typing import Type
from .types import T
import requests
import json


class API(APIProtocol):
    def __init__(
        self,
        base_url: str,
        api_key: SecretStr | None = None,
        extra_headers: dict | None = None,
        extra_params: dict | None = None,
        log_file: str = "log.txt",
    ):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
        }

        if api_key:
            self.headers["Authorization"] = f"Bearer {api_key.get_secret_value()}"

        if extra_headers:
            self.headers.update(extra_headers)

        self.default_params = extra_params or {}

        self.log_file = log_file

    def request(
        self,
        method: str,
        endpoint: str,
        response_type: Type[T],
        params: dict | None = None,
        data: dict | None = None,
    ) -> T:

        url = f"{self.base_url}/{endpoint}"
        merged_params = {**self.default_params, **(params or {})}

        response = requests.request(
            method, url, headers=self.headers, params=merged_params, json=data
        )

        response.raise_for_status()

        json_response = json.dumps(response.json(), ensure_ascii=False)

        print(response)
        print(type(response))

        print("+=+=+=+=+=")

        print(json_response)
        print(type(json_response))

        self._log_request_response(
            method, url, merged_params, data, response.status_code, json_response
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

    def _log_request_response(
        self, method, url, params, data, status_code, response_json
    ):
        """Logs request and response details in JSON format."""
        # Extract endpoint from URL
        endpoint = url.replace(self.base_url, "").strip("/")
        key = f"{method} {endpoint}"

        # Create the log entry as a dictionary
        log_entry = {
            self.base_url: {
                key: {
                    "request": {
                        "headers": {
                            key: "Bearer key" if key == "Authorization" else value
                            for key, value in self.headers.items()
                        },
                        "params": params or {},
                        "data": data,
                    },
                    "response": {"status_code": status_code, "body": response_json},
                }
            }
        }

        # Append to file in JSON format
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write("==========================\n")
            f.write(json.dumps(log_entry, indent=2))
            f.write("\n")
