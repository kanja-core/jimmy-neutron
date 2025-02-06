from typing import List
from typeAliases import LLMPrompt


class PromptMaker:
    def __init__(self, prompt: List[LLMPrompt]):
        self.prompt = prompt

    def exec(self, extraPrompts: List[LLMPrompt]) -> List[LLMPrompt]:
        return self.prompt + extraPrompts
