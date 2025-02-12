from __future__ import annotations
from typing import List, TypeVar, Generic, Dict, Any
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

from ...typeAliases import LLMPrompt  # Keep this if still required

TInputDataclass = TypeVar("TInputDataclass", bound=BaseModel)
TOutputDataclass = TypeVar("TOutputDataclass", bound=BaseModel)


class NodePassInOutput[T](GenericModel):
    data: T


class NodeParserInput(BaseModel):
    file_path: str = Field(
        default="",
        description="Path to the file that needs to be parsed",
    )


class NodeParserOutput(BaseModel):
    text: str = Field(
        default="",
        description="Extracted text content from the parsed file",
    )


class NodeRetrieverInput(BaseModel):
    prompt: List[LLMPrompt] = Field(
        default_factory=list,
        description=(
            "List of prompts to be sent to the LLM. Each prompt must be "
            "a dictionary with 'role' and 'content'. Roles can be 'system', "
            "'user', or 'assistant'."
        ),
        examples=[
            [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What is the capital of France?"},
            ]
        ],
    )


class NodeValidatorOutput(BaseModel):
    status: bool = Field(default=False, description="Status of the validation")


class NodeFetcherInput(BaseModel):
    params: Dict[str, Any]  # Using Dict instead of `dict` for better typing


class NodeFetcherOutput[T](GenericModel):
    data: T


# from __future__ import annotations
# from dataclasses import dataclass, field
# from typing import List, TypeVar
# from ...typeAliases import LLMPrompt

# from typing_extensions import Protocol


# class DataclassProtocol(Protocol):
#     __dataclass_fields__: dict  # minimal: just needs to exist


# TInputDataclass = TypeVar("TInputDataclass", bound=DataclassProtocol)
# TOutputDataclass = TypeVar("TOutputDataclass", bound=DataclassProtocol)


# @dataclass
# class NodePassInOutput[T]:
#     data: T


# @dataclass
# class NodeParserInput:
#     file_path: str = field(
#         default="", metadata={"description": "Path to the file that needs to be parsed"}
#     )


# @dataclass
# class NodeParserOutput:
#     text: str = field(
#         default="",
#         metadata={"description": "Extracted text content from the parsed file"},
#     )


# @dataclass
# class NodeRetrieverInput:
#     prompt: List[LLMPrompt] = field(
#         default_factory=list,
#         metadata={
#             "description": (
#                 "List of prompts to be sent to the LLM. Each prompt must be "
#                 "a dictionary with 'role' and 'content'. Roles can be 'system', "
#                 "'user', or 'assistant'."
#             ),
#             "examples": [
#                 [
#                     {"role": "system", "content": "You are a helpful assistant."},
#                     {"role": "user", "content": "What is the capital of France?"},
#                 ]
#             ],
#         },
#     )


# @dataclass
# class NodeValidatorOutput:
#     status: bool = field(
#         default=False, metadata={"description": "Status of the validation"}
#     )


# @dataclass
# class NodeFetcherInput:
#     params: dict


# # @dataclass
# # class NodeFetcherOutput[T]:
# #     data: T
