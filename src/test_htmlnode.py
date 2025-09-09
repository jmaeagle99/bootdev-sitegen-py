import unittest

from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_to_html_raises_not_implemented(self):
        node = HtmlNode("div", "content")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html_no_props(self):
        node = HtmlNode("div", "content")
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_one_prop(self):
        node = HtmlNode("div", "content", props={"class": "my-class"})
        self.assertEqual(node.props_to_html(), ' class="my-class"')
    
    def test_props_to_html_multiple_props(self):
        node = HtmlNode("div", "content", props={"class": "my-class", "id": "my-id"})
        self.assertEqual(node.props_to_html(), ' class="my-class" id="my-id"')

if __name__ == "__main__":
    unittest.main()