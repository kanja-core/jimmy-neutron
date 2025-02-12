from typing import Callable, Type
from .types import Lawsuits
from ...api.protocol import APIProtocol


class Fetcher[T]:
    """
    A base fetcher that makes API calls and returns structured data.

    Args:
        endpoint (str): The API endpoint to call.
        api (API): The API instance to use.
        fn (Callable): The function to map the response to the output.
    """

    def __init__(self, endpoint: str, api: APIProtocol, fn: Callable):
        self.endpoint = endpoint
        self.api = api
        self.fn = fn

    def exec(self, params: dict) -> T:
        """Makes an API call and returns the output."""
        raise NotImplementedError()


class FetcherLawsuits[T](Fetcher[Lawsuits]):
    """
    A fetcher for lawsuits.
    Args:
        endpoint (str): The API endpoint to call.
        api (API): The API instance to use.
        fn (Callable): The function to map the response to the output.
        cpf_cnpj (str): The ID of the person/company in lawsuit. Either CPF or CNPJ.
    """

    def __init__(
        self,
        endpoint: str,
        api: APIProtocol,
        fn: Callable[[T], Lawsuits],
        api_response_type: Type[T],
    ):
        """"""
        self.api_response_type = api_response_type
        super().__init__(endpoint, api, fn)

    def exec(self, params: dict) -> Lawsuits:
        res = self.api.get(
            self.endpoint, params=params, response_type=self.api_response_type
        )
        return self.fn(res)
