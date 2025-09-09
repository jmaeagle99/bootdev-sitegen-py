from typing import Dict, List

from htmlnode import HtmlNode


class ParentNode(HtmlNode):
    def __init__(self, tag: str, children: List[HtmlNode], props: Dict[str, str] | None = None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        props_str = self.props_to_html()
        children_html = ''.join(child.to_html() for child in self.children)
        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"