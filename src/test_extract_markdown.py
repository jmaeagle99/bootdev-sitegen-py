import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images_empty(self):
        matches = extract_markdown_images(
            ""
        )
        self.assertListEqual([], matches)
    
    def test_extract_markdown_images_none(self):
        matches = extract_markdown_images(
            "I'm a little teapot!"
        )
        self.assertListEqual([], matches)
    
    def test_extract_markdown_images_nourl(self):
        matches = extract_markdown_images(
            "![image]"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_images_notext(self):
        matches = extract_markdown_images(
            "!(https://www.google.com)"
        )
        self.assertListEqual([], matches)
    
    def test_extract_markdown_images_single(self):
        matches = extract_markdown_images(
            "![image](https://www.google.com)"
        )
        self.assertListEqual([("image", "https://www.google.com")], matches)

    def test_extract_markdown_images_single_prefixed(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_single_suffixed(self):
        matches = extract_markdown_images(
            "![Logo](https://i.imgur.com/zjjcJKZ.png) with some text after."
        )
        self.assertListEqual([("Logo", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_single_embedded(self):
        matches = extract_markdown_images(
            "This is text with an ![Python](https://i.imgur.com/zjjcJKZ.png) with some text after."
        )
        self.assertListEqual([("Python", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "Prefix ![Bing](https://www.bing.com) infix ![Google](https://www.google.com) suffix."
        )
        self.assertListEqual([("Bing", "https://www.bing.com"), ("Google", "https://www.google.com")], matches)
    
    def test_extract_markdown_images_mixed(self):
        matches = extract_markdown_images(
            "Prefix ![Bing](https://www.bing.com) infix [Google](https://www.google.com) suffix."
        )
        self.assertListEqual([("Bing", "https://www.bing.com")], matches)
    
    def test_extract_markdown_links_empty(self):
        matches = extract_markdown_links(
            ""
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_links_none(self):
        matches = extract_markdown_links(
            "I'm a little teapot!"
        )
        self.assertListEqual([], matches)
    
    def test_extract_markdown_links_nourl(self):
        matches = extract_markdown_links(
            "[image]"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_links_notext(self):
        matches = extract_markdown_links(
            "(https://www.google.com)"
        )
        self.assertListEqual([], matches)
    
    def test_extract_markdown_links_single(self):
        matches = extract_markdown_links(
            "[image](https://www.google.com)"
        )
        self.assertListEqual([("image", "https://www.google.com")], matches)

    def test_extract_markdown_links_single_prefixed(self):
        matches = extract_markdown_links(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links_single_suffixed(self):
        matches = extract_markdown_links(
            "[Logo](https://i.imgur.com/zjjcJKZ.png) with some text after."
        )
        self.assertListEqual([("Logo", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links_single_embedded(self):
        matches = extract_markdown_links(
            "This is text with an [Python](https://i.imgur.com/zjjcJKZ.png) with some text after."
        )
        self.assertListEqual([("Python", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "Prefix [Bing](https://www.bing.com) infix [Google](https://www.google.com) suffix."
        )
        self.assertListEqual([("Bing", "https://www.bing.com"), ("Google", "https://www.google.com")], matches)
    
    def test_extract_markdown_links_mixed(self):
        matches = extract_markdown_links(
            "Prefix ![Bing](https://www.bing.com) infix [Google](https://www.google.com) suffix."
        )
        self.assertListEqual([("Google", "https://www.google.com")], matches)

if __name__ == "__main__":
    unittest.main()