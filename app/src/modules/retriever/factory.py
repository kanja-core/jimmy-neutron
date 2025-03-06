from .models.models import TaxCertificate, ID
from .models.botActions import BotActions
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
        return RetrieverStructured[TaxCertificate](
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
        return RetrieverStructured[ID](
            LLMFactory.openai(
                model=settings.openai_model,
                api_base=settings.openai_api_base,
                key=settings.openai_api_key,
            ),
            ID,
        )

    @staticmethod
    def botActions() -> RetrieverStructured:
        """Creates a new BotActions Retriever instance"""
        return RetrieverStructured[BotActions](
            LLMFactory.openai(
                model=settings.openai_model,
                api_base=settings.openai_api_base,
                key=settings.openai_api_key,
            ),
            BotActions,
        )
