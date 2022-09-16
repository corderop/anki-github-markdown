import pytest
from unittest.mock import MagicMock, patch
import requests
from markdown_converter.github import GithubMarkdownConverter
from markdown_converter.github.errors import GithubException


class TestGithubMarkdownConverter:
    @patch.object(requests, "post")
    def test_github_markdown(self, mock_post):
        md_text = "# Hello"
        expected_html = """
            <h1>
                <a id="user-content-hello" class="anchor" aria-hidden="true" href="#hello">
                    <span aria-hidden="true" class="octicon octicon-link"></span>
                </a>
                Hello
            </h1>\n
        """
        mock_post.return_value = MagicMock(status_code=200, text=expected_html)

        result = GithubMarkdownConverter().run(md_text)

        assert result == expected_html

    @patch.object(requests, "post")
    def test_github_markdown_empty(self, mock_post):
        mock_post.return_value = MagicMock(status_code=200, text="")

        result = GithubMarkdownConverter().run("")

        assert result == ""

    @patch.object(requests, "post")
    def test_github_markdown_400_error(self, mock_post):
        md_text = "# Goodbye"
        response_text = """{
            "message": "Body should be a JSON object",
            "documentation_url": "https://docs.github.com/rest/reference/markdown#render-a-markdown-document",
        }"""
        mock_post.return_value = MagicMock(status_code=400, text=response_text)

        with pytest.raises(GithubException) as e:
            GithubMarkdownConverter().run(md_text)
            assert e.message == response_text

    @patch.object(requests, "post")
    def test_github_markdown_500_error(self, mock_post):
        md_text = "# Goodbye"
        response_text = """Unexpected error"""
        mock_post.return_value = MagicMock(status_code=500, text=response_text)

        with pytest.raises(GithubException) as e:
            GithubMarkdownConverter().run(md_text)
            assert e.message == response_text
