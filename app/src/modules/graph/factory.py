from typing import List
from .builder import Builder
from ..node.factory import (
    NodeMapperFactory,
    NodeParserFactory,
    NodePassFactory,
    NodeRetrieverFactory,
    NodeValidatorFactory,
)
from ..node.types import (
    NodeParserInput,
    NodeParserOutput,
    NodePassInOutput,
    NodeRetrieverInput,
    NodeValidatorOutput,
)
from ..retriever.models import TaxCertificate
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


def validate_tax_certificate(
    tax_certificate: TaxCertificate,
) -> bool:
    return tax_certificate.debt_exists != "positive"


class BuilderFactory:
    @staticmethod
    def test_1() -> Builder:
        start_node = NodePassFactory[str].get("first", [])

        node_map_start_parse = NodeMapperFactory[
            NodePassInOutput[str], NodeParserInput
        ].get(
            "map_start_parse",
            [start_node],
            fn=lambda x: NodeParserInput(file_path=x.data),
            input_type=NodePassInOutput[str],
        )

        node_parse_tax = NodeParserFactory().text("parse_tax", [node_map_start_parse])

        # node_map_placehold_parser = NodeMapperFactory[
        #     NodeParserInput, NodeParserOutput
        # ].get(
        #     "xyz_placehold_parser",
        #     [node_map_start_parse],
        #     fn=lambda x: NodeParserOutput(text="test: " + x.file_path),
        #     input_type=NodeParserInput,
        # )

        node_map_parse_retrieve_tax = NodeMapperFactory[
            NodeParserOutput, NodeRetrieverInput
        ].get(
            "map_parse_retrieve_tax",
            [node_parse_tax],
            taxPrompt,
            NodeParserOutput,
        )

        node_retrieve_tax = NodeRetrieverFactory[TaxCertificate]().tax_certificate(
            "retrieve_tax", [node_map_parse_retrieve_tax]
        )

        node_validate_output = NodeValidatorFactory[TaxCertificate].get(
            "validate_output",
            [node_retrieve_tax],
            lambda x: x.debt_exists != "positive",
            TaxCertificate,
        )

        node_map_validate_end = NodeMapperFactory[
            NodeValidatorOutput, NodePassInOutput[bool]
        ].get(
            "map_validate_output",
            [node_validate_output],
            lambda x: NodePassInOutput(data=x.status),
            NodeValidatorOutput,
        )

        node_end = NodePassFactory[bool].get("last", [node_map_validate_end])

        return Builder(node_end)
