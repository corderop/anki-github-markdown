class MarkdownIntoHTMLIngestorException(Exception):
    pass


class InvalidHTMLProvided(MarkdownIntoHTMLIngestorException):
    pass


class EmptyHTMLProvided(MarkdownIntoHTMLIngestorException):
    pass
