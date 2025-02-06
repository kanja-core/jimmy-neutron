from .models import TaxCertificate, ID
from .main import RetrieverStructured
from ..llm.factory import LLMFactory
from ...settings.main import settings


class RetrieverFactory:
    """
    A factory class for creating Retriever instances.
    """

    @staticmethod
    def tax_certificate() -> RetrieverStructured:
        """Creates a new CND Retriever instance."""
        return RetrieverStructured(
            LLMFactory.openai(
                model=settings.openai_model,
                api_base=settings.openai_api_base,
                key=settings.openai_api_key,
            ),
            TaxCertificate,
        )

    @staticmethod
    def id() -> RetrieverStructured:
        """Creates a new ID Retriever instance."""
        return RetrieverStructured(
            LLMFactory.openai(
                model=settings.openai_model,
                api_base=settings.openai_api_base,
                key=settings.openai_api_key,
            ),
            ID,
        )
