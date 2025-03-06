import base64
from ..retriever.models.botActions import BotActions
import json
from .builder import Builder
from ..node.factory import (
    NodeMapperFactory,
    NodeParserFactory,
    NodePassFactory,
    NodeRetrieverFactory,
    NodeValidatorFactory,
    NodeFetcherFactory,
)
from ..node.types import (
    NodeFetcherInput,
    NodeFetcherOutput,
    NodeParserInput,
    NodeParserOutput,
    NodePassInOutput,
    NodeRetrieverInput,
    NodeValidatorOutput,
)
from ..retriever.models.models import TaxCertificate
from ..fetcher.types import APIGatewayProxyResultBody, Lawsuits, APIGatewayProxyResult
from .helpers.taxPrompt import taxPrompt
from .helpers.botPrompt import botPrompt


def validate_tax_certificate(
    tax_certificate: TaxCertificate,
) -> bool:
    return tax_certificate.debt_exists != "positive"


def map_bot_save_parse(
    input: APIGatewayProxyResult,
) -> NodeParserInput:
    print("input", input)
    print("input body", input.body)
    data = json.loads(input.body)
    pydantic_model = APIGatewayProxyResultBody(**data)
    print("raw", len(pydantic_model.file))
    pdf_bytes = base64.b64decode(pydantic_model.file)
    print("pdf", len(pdf_bytes))
    # Save the file in binary mode
    with open("/tmp/bot_file.pdf", "wb") as file:  # "wb" means write binary
        file.write(pdf_bytes)
    return NodeParserInput(file_path="/tmp/bot_file.pdf")


class BuilderFactory:
    @staticmethod
    def test_lambda_flow() -> Builder:
        node_start = NodePassFactory[str].get("first", [], str)

        node_map_start_retrieve_actions = NodeMapperFactory[
            NodePassInOutput[str], NodeRetrieverInput
        ].get(
            "node_map_start_retrieve_actions",
            [node_start],
            fn=botPrompt,
            input_type=NodePassInOutput[str],
        )

        node_retrieve_actions = NodeRetrieverFactory[BotActions]().botActions(
            "retrieve_actions", [node_map_start_retrieve_actions]
        )

        node_map_retrieve_fetch = NodeMapperFactory[BotActions, NodeFetcherInput].get(
            "map_start_fetch",
            [node_retrieve_actions],
            # [node_start],
            fn=lambda x: NodeFetcherInput(
                params={
                    "body": {
                        "actions": [action.model_dump() for action in x.bot_actions],
                        # "actions": [{"type":"disableAutoSolve","cat":"captcha","selector":None,"value":None,"timeout":None,"validationURL":None},{"type":"goto","cat":"default","selector":"https://www10.fazenda.sp.gov.br/CertidaoNegativaDeb/Pages/EmissaoCertidaoNegativa.aspx","value":None,"timeout":None,"validationURL":None},{"type":"input","cat":"default","selector":"#MainContent_txtDocumento","value":"52728162859","timeout":None,"validationURL":None},{"type":"solve","cat":"captcha","selector":None,"value":None,"timeout":None,"validationURL":None},{"type":"download","cat":"default","selector":"#MainContent_btnImpressao","value":"/tmp/file.pdf","timeout":None,"validationURL":None}],
                        "request_id": 123,
                    }
                }
            ),
            input_type=BotActions,
            # input_type=NodePassInOutput[str],
        )

        node_fetch_bot = NodeFetcherFactory[APIGatewayProxyResult]().aws_lambda(
            "fetch_bot", [node_map_retrieve_fetch]
        )

        node_map_fetch_parse = NodeMapperFactory[
            APIGatewayProxyResult, NodeParserInput
        ].get(
            "map_fetch_parse",
            [node_fetch_bot],
            map_bot_save_parse,
            APIGatewayProxyResult,
        )

        node_parse_tax = NodeParserFactory().text("parse_tax", [node_map_fetch_parse])

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

        node_end = NodePassFactory[bool].get("last", [node_map_validate_end], bool)

        return Builder(node_end)

    @staticmethod
    def test_parse_retrieve() -> Builder:
        start_node = NodePassFactory[str].get("first", [], str)

        node_map_start_parse = NodeMapperFactory[
            NodePassInOutput[str], NodeParserInput
        ].get(
            "map_start_parse",
            [start_node],
            fn=lambda x: NodeParserInput(file_path=x.data),
            input_type=NodePassInOutput[str],
        )

        node_parse_tax = NodeParserFactory().text("parse_tax", [node_map_start_parse])

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

        node_end = NodePassFactory[bool].get("last", [node_map_validate_end], bool)

        return Builder(node_end)

    @staticmethod
    def test_fetch():
        node_start = NodePassFactory[str].get("first", [], str)

        node_map_start_fetch = NodeMapperFactory[
            NodePassInOutput[str], NodeFetcherInput
        ].get(
            "map_start_fetch",
            [node_start],
            fn=lambda x: NodeFetcherInput(
                params={
                    "cpf_cnpj": x.data,
                }
            ),
            input_type=NodePassInOutput[str],
        )

        node_fetch_lawsuits = NodeFetcherFactory[Lawsuits]().lawsuits(
            "fetch_lawsuits", [node_map_start_fetch]
        )

        node_map_lawsuits_end = NodeMapperFactory[
            Lawsuits, NodePassInOutput[Lawsuits]
        ].get(
            "map_validate_output",
            [node_fetch_lawsuits],
            lambda x: NodePassInOutput(data=x),
            Lawsuits,
        )

        node_end = NodePassFactory[Lawsuits].get(
            "last", [node_map_lawsuits_end], Lawsuits
        )

        return Builder(node_end)
