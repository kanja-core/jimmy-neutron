from typing import Any, List, Callable, Generic, Type
from ..parser.main import Parser
from ..parser.factory import ParserFactory
from ..retriever.main import Retriever
from ..retriever.factory import RetrieverFactory
from .types import (
    TInput,
    TOutput,
    T,
    NodeParserInput,
    NodeRetrieverInput,
    NodePassInOutput,
)
from .main import Node, NodeParser, NodeMapper, NodeValidator, NodeRetriever, NodePass


class NodeParserFactory:
    @staticmethod
    def text(name: str, prev: List[Node[Any, NodeParserInput]]):
        return NodeParser(ParserFactory.text(), name, prev)

    @staticmethod
    def picture(name: str, prev: List[Node[Any, NodeParserInput]]):
        return NodeParser(ParserFactory.picture(), name, prev)


class NodeRetrieverFactory(Generic[TOutput]):
    @staticmethod
    def id(
        name: str, prev: List[Node[Any, NodeRetrieverInput]]
    ) -> NodeRetriever[TOutput]:
        return NodeRetriever[TOutput](RetrieverFactory.id(), name, prev)

    @staticmethod
    def tax_certificate(
        name: str,
        prev: List[Node[Any, NodeRetrieverInput]],
    ) -> NodeRetriever[TOutput]:
        return NodeRetriever[TOutput](RetrieverFactory.tax_certificate(), name, prev)


class NodeMapperFactory(Generic[TInput, TOutput]):
    @staticmethod
    def get(
        name: str,
        prev: List[Node[Any, TInput]],
        fn: Callable[[TInput], TOutput],
        input_type: Type[TInput],
    ):
        return NodeMapper(name, prev, fn, input_type)


class NodeValidatorFactory(Generic[TInput]):
    @staticmethod
    def get(
        name: str,
        prev: List[Node[Any, TInput]],
        fn: Callable[[TInput], bool],
        input_type: Type[TInput],
    ):
        return NodeValidator(name, prev, fn, input_type)


class NodePassFactory(Generic[T]):
    @staticmethod
    def get(name: str, prev: List[Node[Any, NodePassInOutput[T]]]) -> NodePass[T]:
        return NodePass[T](name, prev)
