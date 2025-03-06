from typing import Callable, Type
from .types import Lawsuits
from ...api.protocol import APIProtocol


class GenericFetcher[TIn, TOut]:
    """
    A base fetcher that makes API calls and returns structured data.

    Args:
        endpoint (str): The API endpoint to call.
        api (API): The API instance to use.
        fn (Callable): The function to map the response to the output.
    """

    def __init__(
        self,
        endpoint: str,
        api: APIProtocol,
        api_response_type: Type[TIn],
    ):
        self.endpoint = endpoint
        self.api = api
        self.api_response_type = api_response_type

    def exec(self, params: dict) -> TOut:
        """Makes an API call and returns the output."""
        raise NotImplementedError()


class FetcherMapper[MapIn, MapOut](GenericFetcher[MapIn, MapOut]):
    """
    A fetcher for mapper.
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
        fn: Callable[[MapIn], MapOut],
        api_response_type: Type[MapIn],
    ):
        self.fn = fn
        super().__init__(endpoint, api, api_response_type)

    def exec(self, params: dict) -> MapOut:
        res = self.api.get(
            self.endpoint, params=params, response_type=self.api_response_type
        )
        return self.fn(res)


class Fetcher[T](GenericFetcher[T, T]):
    """
    A fetcher for mapper.
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
        api_response_type: Type[T],
    ):
        super().__init__(endpoint, api, api_response_type)

    def exec(self, params: dict) -> T:
        res = self.api.post(
            self.endpoint, data=params, response_type=self.api_response_type
        )
        return res
