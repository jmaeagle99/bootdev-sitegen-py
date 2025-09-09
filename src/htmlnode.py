from typing import Dict, List, Optional, Self

class HtmlNode:
    def __init__(self, tag: Optional[str] = None, value: Optional[str] = None, children: Optional[List[Self]] = None, props: Optional[Dict[str, str]] = None):
        self.tag = tag
        self.value = value
        self.children = children if children else []
        self.props = props if props else {}
    
    def to_html(self) -> str:
        raise NotImplementedError()
    
    def props_to_html(self) -> str:
        if not self.props:
            return ""
        props_str = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        return f" {props_str}"

    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"
