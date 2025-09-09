from typing import Dict, Required
from pyparsing import Optional
from htmlnode import HtmlNode


class LeafNode(HtmlNode):
    def __init__(self, tag: str, value: str, props: Dict[str, str] | None = None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self) -> str:
        if not self.value:
            raise ValueError("LeafNode must have a value")
        if not self.tag:
            return self.value
        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"