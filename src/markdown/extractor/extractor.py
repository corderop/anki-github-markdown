import base64

from markdown.extractor.errors import (
    InvalidHTMLProvided,
    MarkdownAttributeNotFoundInHTML,
)
from markdown.tools.html import HTMLParserTools
from markdown.tools.html.errors import InvalidAttributeProvided, NoFirstTagFound


class MarkdownFromHTMLExtractor:
    def run(self, html: str) -> str:
        """Extract the encoded markdown present in the md_content attribute

        Args:
            html (str): HTML string where to extract the markdown

        Raises:
            InvalidHTMLProvided: If an invalid HTML is provided. Most of the time it's
                                 because the HTML doesn't have a first tag.
            MarkdownAttributeNotFoundInHTML: If the HTML doesn't have the md_content attribute.

        Returns:
            str: The decoded markdown extracted
        """
        try:
            first_tag = HTMLParserTools(html).find_first_tag()
            encoded_markdown = HTMLParserTools.get_attributes_from_tag(
                first_tag, "md_content"
            )
        except NoFirstTagFound:
            raise InvalidHTMLProvided
        except InvalidAttributeProvided:
            raise MarkdownAttributeNotFoundInHTML

        return base64.b64decode(encoded_markdown).decode("utf-8")
