import unittest
from textnode import TextNode, TextType
from textnode import text_node_to_html_node
from htmlnode import LeafNode

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

    def test_textnode_to_html(self):
        node = TextNode("This is a sample text node", TextType.LINKS, url="https://example.com")
        expected_html = '<a href="https://example.com">This is a sample text node</a>'
        html_node = text_node_to_html_node(node)
        #print("HTML Node:", html_node)  # Debugging line to print the HTML node
        self.assertEqual(LeafNode.to_html(html_node), expected_html)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

        
    def test_textnode_to_html_image(self):
        node = TextNode("this is a sample image that i took", TextType.IMAGES, url="https://example.com/image.jpg")
        expected_html = '<img src="https://example.com/image.jpg" alt="this is a sample image that i took">'
        html_node = text_node_to_html_node(node)

        self.assertEqual(LeafNode.to_html(html_node), expected_html)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://example.com/image.jpg", "alt": "this is a sample image that i took"})# self.assertEqual(html_node.attributes.get("alt"), "this is a sample image that i took")
        self.assertEqual(html_node.value, "")  # For img tag, value should be ""

    def test_textnode_to_html_TEXT(self):
        node = TextNode("this is a plain text with no tag", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value,"this is a plain text with no tag")
        self.assertEqual(html_node.tag, None) # there is likely bug here where leafNode does not allow empty tags but here it has, so when we will convert it to html it will give error


if __name__ == "__main__":
    unittest.main()