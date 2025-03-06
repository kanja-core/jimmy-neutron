from .types import Lawsuits, APIGatewayProxyResult
from .main import Fetcher, GenericFetcher, FetcherMapper
from .mapper import LawsuitFetcherMapper
from .extra.typesEscavador import LawsuitsEscavador
from ...api.factory import APIFactory


class FetcherFactory:
    """
    A factory class for creating Fetcher instances.
    """

    @staticmethod
    def lawsuits() -> GenericFetcher[LawsuitsEscavador, Lawsuits]:
        """Creates a new Fetcher instance with the provided configuration."""
        return FetcherMapper[LawsuitsEscavador, Lawsuits](
            "envolvido/processos",
            APIFactory.escavador_mock(),  # injected mock
            LawsuitFetcherMapper.escavador,
            api_response_type=LawsuitsEscavador,
        )

    @staticmethod
    def aws_lambda() -> Fetcher[APIGatewayProxyResult]:
        """Creates a new Fetcher instance with the provided configuration."""
        return Fetcher(
            "2015-03-31/functions/function/invocations",
            APIFactory.bot(),
            api_response_type=APIGatewayProxyResult,
        )
