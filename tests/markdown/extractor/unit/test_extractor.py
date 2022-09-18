import pytest

from markdown.extractor import MarkdownFromHTMLExtractor
from markdown.extractor.errors import (
    InvalidHTMLProvided,
    MarkdownAttributeNotFoundInHTML,
)


class TestMarkdownFromHTMLExtractor:
    def test_get_markdown_form_html(self):
        html = '<h1 md_content="IyBUZXN0">Test</h1>'
        expected = "# Test"

        result = MarkdownFromHTMLExtractor().run(html)

        assert result == expected

    def test_get_html_without_tag(self):
        html = "<h1>Test</h1>"

        with pytest.raises(MarkdownAttributeNotFoundInHTML):
            MarkdownFromHTMLExtractor().run(html)

    def test_get_invalid_html(self):
        html = "Test"

        with pytest.raises(InvalidHTMLProvided):
            MarkdownFromHTMLExtractor().run(html)
