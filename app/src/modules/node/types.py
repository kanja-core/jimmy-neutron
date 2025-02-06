from __future__ import annotations
from typing import TypeVar, List, Generic
from pydantic import BaseModel, Field
from ...typeAliases import LLMPrompt


TInput = TypeVar("TInput", bound=BaseModel)
TOutput = TypeVar("TOutput", bound=BaseModel)
T = TypeVar("T")


class NodePassInOutput(BaseModel, Generic[T]):
    data: T


class NodeParserInput(BaseModel):
    file_path: str = Field(description="Path to the file that needs to be parsed")


class NodeParserOutput(BaseModel):
    text: str = Field(description="Extracted text content from the parsed file")


class NodeRetrieverInput(BaseModel):
    prompt: List[LLMPrompt] = Field(
        description="List of prompts to be sent to the LLM. Each prompt must be a dictionary with 'role' and 'content' fields."
        "\nRoles can be: 'system', 'user', or 'assistant'.",
        examples=[
            [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What is the capital of France?"},
            ]
        ],
    )


class NodeValidatorOutput(BaseModel):
    status: bool = Field(description="Status of the validation")
