import unittest

from conversions import text_node_to_html_node
from leafnode import LeafNode
from textnode import TextNode, TextType


class TestConversions(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_node_to_html_node_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
    
    def test_text_node_to_html_node_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_text_node_to_html_node_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
    
    def test_text_node_to_html_node_link(self):
        node = TextNode("This is a link node", TextType.LINK, url="http://example.com")
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertIn("href", html_node.props)
        self.assertEqual(html_node.props["href"], "http://example.com")
    
    def test_text_node_to_html_node_image(self):
        node = TextNode("This is the alt text", TextType.IMAGE, url="http://example.com")
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertIn("src", html_node.props)
        self.assertEqual(html_node.props["src"], "http://example.com")
        self.assertIn("alt", html_node.props)
        self.assertEqual(html_node.props["alt"], "This is the alt text")

if __name__ == "__main__":
    unittest.main()