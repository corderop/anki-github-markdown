from unittest.mock import patch

from markdown import MarkdownToggler
from markdown.converter import MarkdownToHTMLConverter


def mock_markdown_converter(return_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with patch.object(
                MarkdownToHTMLConverter, "run", return_value=return_value
            ) as mock:
                return func(*[*args, mock], **kwargs)

        return wrapper

    return decorator


class TestToggler:
    @mock_markdown_converter(return_value="<h1>Test</h1>")
    def test_provide_md(self, *_):
        markdown = "# Test"
        expected = '<h1 md_content="IyBUZXN0">Test</h1>'

        result = MarkdownToggler().run(markdown)

        assert result == expected

    @mock_markdown_converter
    def test_turn_back_to_markdown(self, markdown_converter_mock):
        html = '<h1 md_content="IyBUZXN0">Test</h1>'
        expected = "# Test"

        result = MarkdownToggler().run(html)

        assert result == expected
        markdown_converter_mock.assert_not_called()

    @mock_markdown_converter(return_value="<h1>Test</h1>")
    def test_receive_same_md(self, *_):
        markdown = "# Test"

        toggler = MarkdownToggler()
        html = toggler.run(markdown)
        result = toggler.run(html)

        assert result == markdown

    @mock_markdown_converter(return_value="<h1>Test</h1>")
    def test_html_without_md_content_attribute_considered_as_md(self, *_):
        text = "<h1>Test</h1>"
        expected = '<h1 md_content="PGgxPlRlc3Q8L2gxPg==">Test</h1>'

        result = MarkdownToggler().run(text)

        assert result == expected

    @mock_markdown_converter(
        return_value="""
            <h1>
                <a id="user-content-test" class="anchor" aria-hidden="true" href="#test">
                    <span aria-hidden="true" class="octicon octicon-link"></span>
                </a>
                Test
            </h1>
            <br>
            <div class="highlight highlight-source-python">
                <pre><span class="pl-en">print</span>(<span class="pl-s">"hello"</span>)</pre>
            </div>
        """
    )
    def test_reggression_test_with_multiples_lines_and_br(
        self, markdown_converter_mock
    ):
        text = '# Test<br><br>&lt;br&gt;<br><br>```py<br>print("hello")<br>```'
        expected = '# Test\n\n<br>\n\n```py\n\nprint("hello")\n\n```'

        MarkdownToggler().run(text)

        markdown_converter_mock.assert_called_with(expected)
