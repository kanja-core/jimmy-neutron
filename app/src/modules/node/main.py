from __future__ import annotations
from typing import Any, Generic, List, Callable, Type
from ..parser.main import Parser
from ..retriever.main import Retriever
from .types import (
    NodeValidatorOutput,
    T,
    TInput,
    TOutput,
    NodeParserInput,
    NodeParserOutput,
    NodeRetrieverInput,
    NodePassInOutput,
)
from ...typeAliases import LLMPrompt


def taxPrompt(input: NodeParserOutput) -> NodeRetrieverInput:
    print(input)
    print(input.model_dump_json())
    prompt: List[LLMPrompt] = [
        {
            "role": "system",
            "content": """
            You are an expert at extracting information from Brazilian tax certificates. 
            Extract only the specific information requested. 
            Return null if you cannot find the information with certainty. 
            For the debt_status, look specifically for phrases like 'constam débitos' or 'não constam débitos'. 
            For CPF, ensure it's in the correct format with dots and dash. 
            For certificate_number, ensure that it only has one '-' dash character and no whitespaces.
        """,
        },
        {"role": "user", "content": input.text},
    ]

    return NodeRetrieverInput(prompt=prompt)


class Node(Generic[TInput, TOutput]):
    def __init__(
        self,
        name: str,
        prev: List["Node[Any, TInput]"],
        input_type: Type[TInput],
    ) -> None:
        self.name = name
        self.prev = prev
        self.input_type = input_type

    async def exec(self, state: TInput) -> TOutput:
        raise NotImplementedError()


class NodePass(Generic[T], Node[NodePassInOutput[T], NodePassInOutput[T]]):
    def __init__(
        self,
        name: str,
        prev: List[Node[Any, NodePassInOutput]],
    ) -> None:
        super().__init__(name, prev, NodePassInOutput[T])

    async def exec(self, state: NodePassInOutput[T]) -> NodePassInOutput[T]:
        print("--------- NodePass ---------")
        print("name:", self.name)
        print("input:", state.model_dump_json())
        print("output:", state.model_dump_json())
        return state


class NodeParser(Node[NodeParserInput, NodeParserOutput]):
    def __init__(
        self,
        parser: Parser,
        name: str,
        prev: List[Node[Any, NodeParserInput]],
    ) -> None:
        self.parser = parser
        super().__init__(name, prev, NodeParserInput)

    async def exec(self, state: NodeParserInput) -> NodeParserOutput:
        print("--------- NodeParser ---------")
        print("name:", self.name)
        print("input:", state.model_dump_json())
        file_path = state.file_path
        text = await self.parser.exec(file_path)

        out = NodeParserOutput(text=text)

        print("output:", out.model_dump_json())
        return out


class NodeMapper(Node[TInput, TOutput]):
    def __init__(
        self,
        name: str,
        prev: List[Node[Any, TInput]],
        fn: Callable[[TInput], TOutput],
        input_type: Type[TInput],
    ) -> None:
        self.fn = fn
        super().__init__(name, prev, input_type)

    async def exec(self, state: TInput) -> TOutput:
        print("--------- NodeMapper ---------")
        print("name:", self.name)
        print("input:", state.model_dump_json())
        out = self.fn(state)
        print("output:", out.model_dump_json())
        return out


class NodeRetriever(Generic[TOutput], Node[NodeRetrieverInput, TOutput]):
    def __init__(
        self,
        retriever: Retriever,
        name: str,
        prev: List[Node[Any, NodeRetrieverInput]],
    ) -> None:
        self.retriever = retriever
        super().__init__(name, prev, NodeRetrieverInput)

    async def exec(self, state: NodeRetrieverInput) -> TOutput:
        print("--------- NodeRetriever ---------")
        print("name:", self.name)
        print("input:", state.model_dump_json())
        out = self.retriever.exec(state.prompt)
        print("output:", out.model_dump_json())
        return out


class NodeValidator(Node[TInput, NodeValidatorOutput]):
    def __init__(
        self,
        name: str,
        prev: List[Node[Any, TInput]],
        fn: Callable[[TInput], bool],
        input_type: Type[TInput],
    ) -> None:
        self.fn = fn
        super().__init__(name, prev, input_type)

    async def exec(self, state: TInput) -> NodeValidatorOutput:
        print("--------- NodeValidator ---------")
        print("name:", self.name)
        print("input:", state.model_dump_json())
        out = NodeValidatorOutput(status=self.fn(state))
        print("output:", out.model_dump_json())
        return out
