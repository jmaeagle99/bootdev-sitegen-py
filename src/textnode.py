from enum import Enum

from pyparsing import Optional

class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = 5
    IMAGE = 6

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text : str = text
        self.text_type : TextType = text_type
        self.url : str | None = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text, self.text_type, self.url) == (other.text, other.text_type, other.url)

    def __repr__(self):
        return f"TextNode({self.text!r}, {self.text_type}, {self.url})"