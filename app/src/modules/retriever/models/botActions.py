# schemas.py

from pydantic import BaseModel, Field
from typing import Optional, List, Union, Literal
from enum import Enum

#
# 1) Convert the Zod enums into Python Enums
#


class BotActionClassEnum(str, Enum):
    default = "default"
    captcha = "captcha"
    debug = "debug"


class BotActionCaptchaTypeEnum(str, Enum):
    wait = "wait"
    solve = "solve"
    disableAutoSolve = "disableAutoSolve"


class BotActionDebugTypeEnum(str, Enum):
    screenshot = "screenshot"
    url = "url"


#
# 2) Convert the z.union(...) of string literals + Enums into a Python Union
#
#    This union says the `type` can be one of:
#      "form", "click", "delay", "goto", "input", "download"
#      or one of the two Enums: BotActionCaptchaTypeEnum, BotActionDebugTypeEnum
#

BotActionType = Union[
    Literal["form"],
    Literal["click"],
    Literal["delay"],
    Literal["goto"],
    Literal["input"],
    Literal["download"],
    BotActionCaptchaTypeEnum,
    BotActionDebugTypeEnum,
]

#
# 3) The BotActionSchema from Zod becomes a Pydantic model
#
#    - Use "class_" (or something similar) for the "class" property, since
#      "class" is reserved in Python. We can alias it so JSON parsing still works.
#


class BotAction(BaseModel):
    type: BotActionType
    cat: BotActionClassEnum
    selector: Optional[str]
    value: Optional[str]
    timeout: Optional[int]
    validationURL: Optional[str]


#
# 4) The BotActionListObjectSchema becomes:
#


class BotActionListObject(BaseModel):
    actions: List[BotAction]


#
# 5) In your TypeScript code, you also have a "BotActionsSchema"
#    which is essentially { bot_actions: z.array(BotActionSchema) }.
#    You can model that here as well if needed:
#


class BotActions(BaseModel):
    bot_actions: List[BotAction]
