import pytest

from markdown.ingestor import MarkdownIntoHTMLIngestor
from markdown.ingestor.errors import EmptyHTMLProvided, InvalidHTMLProvided


class TestMarkdownIntoHTMLIngestor:
    def test_save_markdown_in_html_md_content_attribute(self):
        html = "<h1>Test</h1>"
        md = "# Test"
        expected = '<h1 md_content="IyBUZXN0">Test</h1>'

        result = MarkdownIntoHTMLIngestor().run(html, md)

        assert result == expected

    def test_add_attribute_with_empty_markdown(self):
        html = "<div></div>"
        md = ""
        expected = '<div md_content=""></div>'

        result = MarkdownIntoHTMLIngestor().run(html, md)

        assert result == expected

    def test_send_empty_html(self):
        html = ""
        md = "# Test"

        with pytest.raises(EmptyHTMLProvided):
            MarkdownIntoHTMLIngestor().run(html, md)

    def test_send_html_without_tags(self):
        html = "Test"
        md = "# Test"

        with pytest.raises(InvalidHTMLProvided):
            MarkdownIntoHTMLIngestor().run(html, md)

    def test_with_unclosed_tab(self):
        html = "<div><h1>Test</h1>"
        md = "# Test"
        expected = '<div md_content="IyBUZXN0"><h1>Test</h1></div>'

        result = MarkdownIntoHTMLIngestor().run(html, md)

        assert result == expected
