from unittest.mock import patch

from markdown import MarkdownToggler
from markdown.converter import MarkdownToHTMLConverter


def mock_markdown_converter(return_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with patch.object(
                MarkdownToHTMLConverter, "run", return_value=return_value
            ):
                return func(*args, **kwargs)

        return wrapper

    return decorator


class TestToggler:
    @mock_markdown_converter(return_value="<h1>Test</h1>")
    def test_provide_md(self):
        markdown = "# Test"
        expected = "<h1>Test</h1>"

        result = MarkdownToggler().run(markdown)

        assert result == expected

    @mock_markdown_converter(return_value="<h1>Test</h1>")
    def test_receive_same_md(self):
        markdown = "# Test"

        toggler = MarkdownToggler()
        html = toggler.run(markdown)
        result = toggler.run(html)

        assert result == markdown
