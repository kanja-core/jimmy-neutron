from typing import Type, TypeVar, Protocol

T = TypeVar("T")


class APIProtocol(Protocol):
    base_url: str
    headers: dict
    default_params: dict
    log_file: str

    def request(
        self,
        method: str,
        endpoint: str,
        response_type: Type[T],
        params: dict | None = None,
        data: dict | None = None,
    ) -> T: ...

    def get(
        self,
        endpoint: str,
        response_type: Type[T],
        params: dict | None = None,
    ) -> T: ...

    def post(
        self,
        endpoint: str,
        response_type: Type[T],
        data: dict | None = None,
    ) -> T: ...

    def put(
        self,
        endpoint: str,
        response_type: Type[T],
        data: dict | None = None,
    ) -> T: ...

    def delete[T](self, endpoint: str, response_type: Type[T]) -> T: ...
