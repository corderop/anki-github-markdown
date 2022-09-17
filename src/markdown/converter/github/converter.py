import requests

from .errors import GithubException


class GithubMarkdownToHTMLConverter:
    def run(self, md_text: str) -> str:
        response = requests.post(
            "https://api.github.com/markdown", json={"text": md_text}
        )

        if response.status_code == 200:
            return response.text

        raise GithubException(response.text)
