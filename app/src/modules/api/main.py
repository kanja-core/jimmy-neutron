from pydantic import SecretStr
from typing import Union, Dict, Type
from ...universal.types import T
import requests


class API:
    def __init__(
        self,
        base_url: str,
        api_key: SecretStr | None = None,
        extra_headers: dict | None = None,
        extra_params: dict | None = None,
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

    def request(
        self,
        method: str,
        endpoint: str,
        params: dict | None = None,
        data: dict | None = None,
        response_type: Type[T] = dict,  # Specify the return type dynamically
    ) -> T:
        url = f"{self.base_url}/{endpoint}"
        merged_params = {**self.default_params, **(params or {})}

        response = requests.request(
            method, url, headers=self.headers, params=merged_params, json=data
        )

        response.raise_for_status()

        json_response = response.json()

        # Convert the JSON response to the specified type
        if response_type is dict:
            return json_response  # Default behavior
        return response_type(**json_response)

    def get(
        self, endpoint: str, params: dict | None = None, response_type: Type[T] = dict
    ) -> T:
        return self.request("GET", endpoint, params=params, response_type=response_type)

    def post(
        self, endpoint: str, data: dict | None = None, response_type: Type[T] = dict
    ) -> T:
        return self.request("POST", endpoint, data=data, response_type=response_type)

    def put(
        self, endpoint: str, data: dict | None = None, response_type: Type[T] = dict
    ) -> T:
        return self.request("PUT", endpoint, data=data, response_type=response_type)

    def delete(self, endpoint: str, response_type: Type[T] = dict) -> T:
        return self.request("DELETE", endpoint, response_type=response_type)
