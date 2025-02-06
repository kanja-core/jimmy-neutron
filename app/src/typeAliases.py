from typing import Any, TypeAlias, Literal, List, TypeVar
from typing_extensions import TypedDict
from langchain_openai import ChatOpenAI
from llama_parse import LlamaParse
from pydantic import BaseModel

LLMType: TypeAlias = Literal["openai", "claude", "other"]
LLM: TypeAlias = ChatOpenAI | Any

LLMPromptCaller: TypeAlias = Literal["system", "user", "assistant"]


# Define the structure of a message
class LLMPrompt(TypedDict):
    role: LLMPromptCaller
    content: str


class LLMInput(TypedDict):
    messages: List[LLMPrompt]


ParserType: TypeAlias = Literal["llama", "other"]
GenericParser: TypeAlias = LlamaParse | Any

T_PYDANTYC = TypeVar("T_PYDANTYC", bound=BaseModel)
T = TypeVar("T")
