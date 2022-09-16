from abc import ABC, abstractmethod


class MarkdownConverterService(ABC):
    @abstractmethod
    def run(self, md_text: str) -> str:
        pass
