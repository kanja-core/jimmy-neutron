from langgraph.constants import END, START
from langgraph.graph.state import CompiledStateGraph, StateGraph
from ..node.main import Node
from ..node.types import (
    NodePassInOutput,
    NodeParserInput,
    NodeParserOutput,
    NodeRetrieverInput,
    NodeValidatorOutput,
)
from typing import Set, TypeVar


# class GeneralState(
#     NodePassInOutput[str],
#     NodeParserInput,
#     # NodeParserOutput,
#     # NodeRetrieverInput,
#     # NodeValidatorOutput,
# ):
#     pass


class Builder:
    """Graph builder base class."""

    def __init__(self, end_node: Node):
        self.end_node = end_node
        self.graph: CompiledStateGraph | None = None

    def exec(self) -> CompiledStateGraph:
        """Builds the processing graph using langgraph."""
        # 1. Collect all nodes by traversing backwards (from end_node to its parents)
        all_nodes = self._gather_all_nodes(self.end_node)

        # 2. Build the StateGraph
        builder = StateGraph(input=NodePassInOutput[str], output=NodePassInOutput[bool])
        # builder = StateGraph(GeneralState)

        # 3. Add nodes and edges to the StateGraph
        for node in all_nodes:
            builder.add_node(node=node.name, action=node.exec, input=node.input_type)

        for node in all_nodes:

            builder.add_edge([prev_node.name for prev_node in node.prev], node.name)

            if node.name == "first":
                builder.add_edge(START, node.name)
            if node.name == "last":
                builder.add_edge(node.name, END)

        # 4. Compile the StateGraph
        self.graph = builder.compile()

        return self.graph

    def _gather_all_nodes(self, end_node: Node) -> list[Node]:
        """
        Reverse traverses the DAG starting from 'end_node' to collect
        all ancestors in topological order.
        """
        visited: Set[Node] = set()
        topological_order: list[Node] = []

        # We can do a DFS or BFS here; we'll use DFS for simplicity
        stack = [end_node]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                topological_order.append(current)
                for p in current.prev:
                    stack.append(p)

        # 'topological_order' is in reverse topological order from DFS.
        topological_order.reverse()
        return topological_order
