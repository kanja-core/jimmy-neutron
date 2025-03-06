from typing import Any, List, Callable, Type
from ..parser.factory import ParserFactory
from ..retriever.factory import RetrieverFactory
from ..fetcher.factory import FetcherFactory
from .types import (
    NodeParserInput,
    NodeRetrieverInput,
    NodePassInOutput,
    NodeFetcherInput,
)
from .main import (
    Node,
    NodeFetcher,
    NodeParser,
    NodeMapper,
    NodeValidator,
    NodeRetriever,
    NodePass,
)


class NodeParserFactory:
    @staticmethod
    def text(name: str, prev: List[Node[Any, NodeParserInput]]):
        return NodeParser(ParserFactory.text(), name, prev)

    @staticmethod
    def picture(name: str, prev: List[Node[Any, NodeParserInput]]):
        return NodeParser(ParserFactory.picture(), name, prev)


class NodeRetrieverFactory[TOutput]:
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

    @staticmethod
    def botActions(
        name: str,
        prev: List[Node[Any, NodeRetrieverInput]],
    ) -> NodeRetriever[TOutput]:
        return NodeRetriever[TOutput](RetrieverFactory.botActions(), name, prev)


class NodeMapperFactory[TInput, TOutput]:
    @staticmethod
    def get(
        name: str,
        prev: List[Node[Any, TInput]],
        fn: Callable[[TInput], TOutput],
        input_type: Type[TInput],
    ):
        return NodeMapper(name, prev, fn, input_type)


class NodeValidatorFactory[TInput]:
    @staticmethod
    def get(
        name: str,
        prev: List[Node[Any, TInput]],
        fn: Callable[[TInput], bool],
        input_type: Type[TInput],
    ):
        return NodeValidator(name, prev, fn, input_type)


class NodePassFactory[T]:
    @staticmethod
    def get(
        name: str,
        prev: List[Node[Any, NodePassInOutput[T]]],
        input_type: Type[T],
    ) -> NodePass[T]:
        return NodePass[T](name, prev, input_type)


class NodeFetcherFactory[T]:
    @staticmethod
    def lawsuits(name: str, prev: List[Node[Any, NodeFetcherInput]]) -> NodeFetcher[T]:
        return NodeFetcher[T](fetcher=FetcherFactory.lawsuits(), name=name, prev=prev)

    @staticmethod
    def aws_lambda(
        name: str,
        prev: List[Node[Any, NodeFetcherInput]],
    ) -> NodeFetcher[T]:
        return NodeFetcher[T](fetcher=FetcherFactory.aws_lambda(), name=name, prev=prev)
