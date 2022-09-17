import base64

from bs4 import BeautifulSoup, Tag


class MarkdownIngestor:
    def __find_first_tag_in_html_tree(self, tree):
        for c in tree.children:
            if type(c) is Tag:
                return c
        return None

    def run(self, html, markdown):
        html_tree = BeautifulSoup(html, "html.parser")
        first_tag = self.__find_first_tag_in_html_tree(html_tree)

        encoded_markdown = base64.b64encode(markdown.encode("utf-8")).decode()
        first_tag["md_content"] = encoded_markdown

        return str(html_tree)
