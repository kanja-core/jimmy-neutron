from pydantic import BaseModel
from typing import TypeVar

T = TypeVar("T", bound=BaseModel)
