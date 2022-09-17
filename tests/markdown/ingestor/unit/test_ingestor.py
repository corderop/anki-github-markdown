from markdown.ingestor import MarkdownIngestor


class TestMarkdownIngestor:
    def test_save_markdown_in_html_md_content_attribute(self):
        html = "<h1>Test</h1>"
        md = "# Test"
        expected = '<h1 md_content="IyBUZXN0">Test</h1>'

        result = MarkdownIngestor().run(html, md)

        assert result == expected
