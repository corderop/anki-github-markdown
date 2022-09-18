class MarkdownFromHTMLExtractor(Exception):
    pass


class MarkdownAttributeNotFoundInHTML(MarkdownFromHTMLExtractor):
    pass


class InvalidHTMLProvided(MarkdownFromHTMLExtractor):
    pass
