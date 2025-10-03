import unittest

from splits import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplits(unittest.TestCase):
    def test_split_nodes_delimiter_code_middle(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, " word")
    
    def test_split_nodes_delimiter_code_start(self):
        node = TextNode("`code` at beginning", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, "")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, " at beginning")
    
    def test_split_nodes_delimiter_code_end(self):
        node = TextNode("Text with cod at end: `code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, "Text with cod at end: ")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, "")
    
    def test_split_nodes_delimiter_code_multiple(self):
        node = TextNode("Text with two code (`codeA` and `codeB`) blocks", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, "Text with two code (")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[1].text, "codeA")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, " and ")
        self.assertEqual(new_nodes[3].text_type, TextType.CODE)
        self.assertEqual(new_nodes[3].text, "codeB")
        self.assertEqual(new_nodes[4].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[4].text, ") blocks")
    
    def test_split_nodes_delimiter_code_unpaired(self):
        node = TextNode("Text with ` one delimiter", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

if __name__ == "__main__":
    unittest.main()