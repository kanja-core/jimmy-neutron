from pydantic import SecretStr
from ...typeAliases import GenericParser
from ...settings.main import settings
from llama_parse import LlamaParse, ResultType
from .main import Parser


class ParserFactory:
    """
    A factory class for creating Parser instances.
    """

    @staticmethod
    def text() -> Parser:
        """Creates a new Parser instance for text parsing."""
        return Parser(
            GenericParserFactory.llama(
                base_url=settings.llamaparse_api_base,
                key=settings.llamaparse_api_key,
                webhook_url=settings.llamaparse_webhook_url,
                fast_mode=True,
                result_type=ResultType.TXT,
            )
        )

    @staticmethod
    def picture() -> Parser:
        """Creates a new Parser instance optimized for document ID."""
        return Parser(
            GenericParserFactory.llama(
                base_url=settings.llamaparse_api_base,
                key=settings.llamaparse_api_key,
                webhook_url=settings.llamaparse_webhook_url,
                fast_mode=False,
                result_type=ResultType.MD,
            )
        )


class GenericParserFactory:
    """
    A factory class for creating Generic Parser instances.
    """

    @staticmethod
    def llama(
        base_url: str,
        key: SecretStr,
        fast_mode: bool = False,
        webhook_url=None,
        result_type=ResultType.TXT,
    ) -> GenericParser:
        return LlamaParse(
            base_url=base_url,
            api_key=key.get_secret_value(),
            result_type=result_type,
            fast_mode=fast_mode,
            webhook_url=webhook_url,
            verbose=False,
            show_progress=False,
        )
