from typing import List
from ...node.types import (
    NodeParserOutput,
    NodeRetrieverInput,
)
from ....typeAliases import LLMPrompt


def taxPrompt(input: NodeParserOutput) -> NodeRetrieverInput:
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
