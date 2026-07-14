import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a sample text node", TextType.PLAIN, url="https://example.com")
        node2 = TextNode("This is a different text node", TextType.PLAIN,  url="https://example.com")
        self.assertNotEqual(node, node2)

    def test_noteq_different_type(self):
        node = TextNode("This is a same sample text node", TextType.PLAIN, url="https://example.com")
        node2 = TextNode("This is a same sample text node", TextType.BOLD, url="https://example.com")
        self.assertNotEqual(node, node2)

    def test_noteq_different_url(self):
        node = TextNode("This is a same sample text node", TextType.PLAIN, url="https://example.com")
        node2 = TextNode("This is a same sample text node", TextType.PLAIN, url="https://different.com")
        self.assertNotEqual(node, node2)

    def test_noteq_different_url_none(self):
        node = TextNode("This is a same sample text node", TextType.PLAIN, url="https://example.com")
        node2 = TextNode("This is a same sample text node", TextType.PLAIN)
        self.assertNotEqual(node, node2)
    def test_noteq_allfields_different(self):
        node = TextNode("This is a same sample text node", TextType.PLAIN, url="https://example.com")
        node2 = TextNode("This is a different sample text node", TextType.BOLD, url="https://different.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()