from dataclasses import is_dataclass


def is_dataclass_instance(cls):
    if is_dataclass(cls) and not isinstance(cls, type):
        return cls
    return None
