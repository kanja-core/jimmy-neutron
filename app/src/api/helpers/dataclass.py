import dataclasses
from typing import Protocol, TypeVar, Type, Any


class DataclassProtocol(Protocol):
    __dataclass_fields__: dict[str, Any]


T = TypeVar("T", bound=DataclassProtocol)


def dataclass_from_dict(cls: Type[T], data: dict) -> T:
    print(cls)
    print(type(cls))
    fieldtypes = {f.name: f.type for f in dataclasses.fields(cls)}  # type: ignore
    return cls(**{f: dataclass_from_dict(fieldtypes[f], data[f]) for f in data})  # type: ignore
