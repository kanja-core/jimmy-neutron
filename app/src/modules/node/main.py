from typing import Any, List, Callable, Type
from ..parser.main import Parser
from ..retriever.main import Retriever
from .types import (
    NodeValidatorOutput,
    NodeParserInput,
    NodeParserOutput,
    NodeRetrieverInput,
    NodePassInOutput,
    NodeFetcherInput,
)
from ..fetcher.main import GenericFetcher


class Node[TInput, TOutput]:
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


class NodePass[T](Node[NodePassInOutput[T], NodePassInOutput[T]]):
    def __init__(
        self, name: str, prev: List[Node[Any, NodePassInOutput]], input_type: Type[T]
    ) -> None:
        super().__init__(name, prev, NodePassInOutput[input_type])

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


class NodeMapper[TInput, TOutput](Node[TInput, TOutput]):
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
        print("input:", state.model_dump_json())  # type: ignore
        out = self.fn(state)
        print("output:", out.model_dump_json())  # type: ignore
        return out


class NodeRetriever[TOutput](Node[NodeRetrieverInput, TOutput]):
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


class NodeValidator[TInput](Node[TInput, NodeValidatorOutput]):
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
        print("input:", state.model_dump_json())  # type: ignore
        out = NodeValidatorOutput(status=self.fn(state))
        print("output:", out.model_dump_json())
        return out


class NodeFetcher[TOutput](Node[NodeFetcherInput, TOutput]):
    def __init__(
        self,
        fetcher: GenericFetcher,
        name: str,
        prev: List[Node[Any, NodeFetcherInput]],
    ) -> None:
        self.fetcher = fetcher
        super().__init__(name, prev, NodeFetcherInput)

    async def exec(self, state: NodeFetcherInput) -> TOutput:
        print("--------- NodeFetcher ---------")
        print("name:", self.name)
        print("input:", state.model_dump_json())
        out = self.fetcher.exec(state.params)
        print("output:", out.model_dump_json())
        return out
