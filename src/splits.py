from typing import List
from extract_markdown import extract_markdown_images, extract_markdown_links
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

def split_nodes_image(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        remaining_text = node.text
        for (text, url) in images:
            pre_image_text, _, post_image_text = remaining_text.partition(f"![{text}]({url})")
            if pre_image_text:
                new_nodes.append(TextNode(pre_image_text, TextType.TEXT))
            new_nodes.append(TextNode(text, TextType.IMAGE, url=url))
            remaining_text = post_image_text
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        remaining_text = node.text
        for (text, url) in links:
            pre_link_text, _, post_link_text = remaining_text.partition(f"[{text}]({url})")
            if pre_link_text:
                new_nodes.append(TextNode(pre_link_text, TextType.TEXT))
            new_nodes.append(TextNode(text, TextType.LINK, url=url))
            remaining_text = post_link_text
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes