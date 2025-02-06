from ...typeAliases import GenericParser


class Parser:
    def __init__(self, parser: GenericParser) -> None:
        self.parser = parser

    async def exec(self, file_path: str) -> str:
        """Parses a file and extracts text."""
        return await self._parse(file_path)

    async def _parse(self, file_path: str) -> str:
        """Parses a file using LlamaParse and extracts text."""
        doc = await self.parser.aload_data(file_path)
        text = doc[0].text_resource.text if doc and doc[0].text_resource else None
        if not text:
            raise ValueError("LLamaParse: No text found")

        return text
