from typing import Union, List, Dict, Optional
from pydantic import BaseModel


class Case(BaseModel):
    cnj: str
    amount: Optional[float] = None
    area: Optional[str] = None


class Involved(BaseModel):
    name: str
    type: str


class Lawsuits(Involved):
    items: list[Case]


class APIGatewayProxyResultBody(BaseModel):
    file: str
    request_id: str | int


class APIGatewayProxyResult(BaseModel):
    statusCode: int
    headers: Optional[Dict[str, Union[bool, int, str]]] = None
    multiValueHeaders: Optional[Dict[str, List[Union[bool, int, str]]]] = None
    body: str
    isBase64Encoded: Optional[bool] = None


# class


# from dataclasses import dataclass
# from typing import Optional


# @dataclass
# class Case:
#     cnj: str
#     amount: Optional[float] = None
#     area: Optional[str] = None


# @dataclass
# class Involved:
#     name: str
#     type: str


# @dataclass
# class Lawsuits(Involved):
#     items: list[Case]
