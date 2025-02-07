from typing import List, Type
from ...typeAliases import LLM, LLMPrompt


class Retriever[T]:
    """
    A base retriever that uses a generic LLM.
    """

    def __init__(self, llm: LLM):
        self.llm = llm

    def exec(self, prompt: List[LLMPrompt]) -> T:
        """Calls the LLM and returns the output."""
        raise NotImplementedError


class RetrieverText(Retriever[str]):
    """
    A retriever that uses a text-based LLM and returns a string.
    """

    def exec(self, prompt: List[LLMPrompt]) -> str:
        """Calls the LLM and returns string output."""
        return self.llm.invoke(prompt)  # type: ignore


class RetrieverStructured[T](Retriever[T]):
    """
    A specialized retriever that uses a structured LLM and returns a Pydantic model.
    """

    def __init__(self, llm: LLM, schema: Type[T]) -> None:
        structured_llm = llm.with_structured_output(schema=schema)
        super().__init__(structured_llm)
        self.schema = schema

    def exec(self, prompt: List[LLMPrompt]) -> T:
        """Calls the structured LLM and returns a parsed Pydantic model."""
        model: T_PYDANTYC = self.llm.invoke(prompt)  # type: ignore
        return model
