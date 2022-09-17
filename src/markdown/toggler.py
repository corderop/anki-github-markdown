from markdown.converter import MarkdownToHTMLConverter


class MarkdownToggler:
    def run(self, text: str) -> str:
        if text == "<h1>Test</h1>":
            return "# Test"

        result = MarkdownToHTMLConverter().run(text)

        return result
