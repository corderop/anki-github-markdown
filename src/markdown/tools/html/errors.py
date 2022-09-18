class HTMLParserToolsException(Exception):
    pass


class InvalidHtmlProvidedForParsing(HTMLParserToolsException):
    pass


class EmptyHtmlProvidedForParsing(InvalidHtmlProvidedForParsing):
    pass


class NoFirstTagFound(HTMLParserToolsException):
    pass


class TagNotFoundInHTML(HTMLParserToolsException):
    pass


class InvalidAttributeProvided(HTMLParserToolsException):
    pass


class InvalidContentProvided(HTMLParserToolsException):
    pass


class InvalidTagProvided(HTMLParserToolsException):
    pass
