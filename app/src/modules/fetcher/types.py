from typing import Optional
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
