from typing import List
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: List[TextNode], delimiter: str, text_type: TextType) -> List[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError("invalid Markdown syntax: unmatched delimiter")
            for index, part in enumerate(parts):
                if index % 2 == 1:
                    new_nodes.append(TextNode(part, text_type))
                else:
                    new_nodes.append(TextNode(part, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes