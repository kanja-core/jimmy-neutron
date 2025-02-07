import json
from dataclasses import is_dataclass
from dataclasses import asdict


def print_dataclass_instance(cls):
    if is_dataclass(cls) and not isinstance(cls, type):
        print("input:", json.dumps(asdict(cls)))
    else:
        print("input:", json.dumps(cls))
