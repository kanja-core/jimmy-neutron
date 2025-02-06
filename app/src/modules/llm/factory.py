from ...typeAliases import LLM
from langchain_openai import ChatOpenAI
from pydantic import SecretStr


class LLMFactory:
    """
    A factory class for creating LLM instances.
    """

    @staticmethod
    def openai(
        model: str, api_base: str, key: SecretStr, max_tokens: int = 1024
    ) -> LLM:
        """Creates an LLM instance based on the given type."""
        llm = ChatOpenAI(
            model=model,
            openai_api_key=key.get_secret_value(),  # type: ignore
            openai_api_base=api_base,  # type: ignore
            max_tokens=max_tokens,  # type: ignore
        )
        return llm
