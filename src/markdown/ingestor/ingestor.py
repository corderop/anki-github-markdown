import base64

from ..tools.html import HTMLParserTools
from ..tools.html.errors import (
    EmptyHtmlProvidedForParsing,
    NoFirstTagFound,
    TagNotFoundInHTML,
)
from .errors import EmptyHTMLProvided, InvalidHTMLProvided


class MarkdownIntoHTMLIngestor:
    def run(self, html: str, markdown: str) -> str:
        """Add the base64 encoded markdown in an attribute
        called md_content inside the first tag of the HTML provided.

        Args:
            html (str): HTML code in which to include the markdown.
            markdown (str): Markdown code to be included in the HTML.

        Raises:
            EmptyHTMLProvided: If empty or None HTML is provided.
            InvalidHTMLProvided: If the HTML provided has no tags or is invalid.

        Returns:
            str: HTML code with the markdown included in the first tag.
        """
        encoded_markdown = base64.b64encode(markdown.encode("utf-8")).decode()

        try:
            html_parser = HTMLParserTools(html)
            first_tag = html_parser.find_first_tag()
            html_parser.add_attribute_to_tag(first_tag, "md_content", encoded_markdown)
        except EmptyHtmlProvidedForParsing:
            raise EmptyHTMLProvided
        except (TagNotFoundInHTML, NoFirstTagFound):
            raise InvalidHTMLProvided

        return html_parser.get_html()
