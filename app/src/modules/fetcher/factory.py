from .types import Lawsuits
from .main import Fetcher, FetcherLawsuits
from .mapper import LawsuitFetcherMapper
from .extra.typesEscavador import LawsuitsEscavador
from ..api.factory import APIFactory


class FetcherFactory:
    """
    A factory class for creating Fetcher instances.
    """

    @staticmethod
    def lawsuits() -> Fetcher[Lawsuits]:
        """Creates a new Fetcher instance with the provided configuration."""
        return FetcherLawsuits[LawsuitsEscavador](
            "envolvido/processos",
            APIFactory.escavador(),
            LawsuitFetcherMapper.escavador,
        )
