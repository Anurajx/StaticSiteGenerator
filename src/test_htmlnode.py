import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode(tag="div", value="Hello", children=[], props={"class": "mynewclass"})
        node2 = HTMLNode(tag="div", value="Hello", children=[], props={"class": "mynewclass"})
        self.assertEqual(node1, node2)
    
    def test_not_eq(self):
        node1 = HTMLNode(tag="div", value="Hello", children=[], props={"class": "mynewclass"})
        node2 = HTMLNode(tag="div", value="Go-away-Dev", children=[], props={"class": "mynewclass"})
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "mynewclass"})
        #print(repr(node))
        expected_repr = "HTMLNode(tag=div, value=Hello, children=[], props={'class': 'mynewclass'})"
        self.assertEqual(repr(node), expected_repr)

    def test_props_to_html(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "mynewclass", "id": "my-id"})
        expected_html = 'class="mynewclass" id="my-id"'
        self.assertEqual(node.props_to_html(), expected_html)

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode(tag="img", value="image.png", props={"alt": "my image"})
        node2 = LeafNode(tag="img", value="image.png", props={"alt": "my image"})
        self.assertEqual(node1, node2)
    
    def test_not_eq(self):
        node1 = LeafNode(tag="img", value="image.png", props={"alt": "my image"})
        node2 = LeafNode(tag="img", value="different.png", props={"alt": "my image"})
        self.assertNotEqual(node1, node2)
    
    def test_repr(self):
        node = LeafNode(tag="img", value="image.png", props={"alt": "my image"})
        expected_repr = "LeafNode(tag=img, value=image.png, props={'alt': 'my image'})"
        self.assertEqual(repr(node), expected_repr)

class TestHTMLParentNode(unittest.TestCase):
    def test_eq(self):
        node1 = ParentNode(tag="div", children=[], props={"class": "mynewclass"})
        node2 = ParentNode(tag="div", children=[], props={"class": "mynewclass"})
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = ParentNode(tag="div", children=[], props={"class": "mynewclass"})
        node2 = ParentNode(tag="div", children=[], props={"class": "differentclass"})
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = ParentNode(tag="div", children=[], props={"class": "mynewclass"})
        expected_repr = "HTMLNode(tag=div, value=None, children=None, props={'class': 'mynewclass'})"
        self.assertEqual(repr(node), expected_repr)

    def test_recursive_children(self):
        child1 = LeafNode(tag="p", value="Hello", props={"class": "child"})
        child2 = LeafNode(tag="p", value="World", props={"class": "child"})
        parent = ParentNode(tag="div", children=[child1, child2], props={"class": "parent"})
        expected_html = '<div class="parent"><p class="child">Hello</p> <p class="child">World</p></div>'
        self.assertEqual(parent.to_html(), expected_html)
    
    def test_parentNodeWithNoChildren(self):
        parent = ParentNode(tag="div", children=[], props={"class": "parent"})
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_parentNodeWithNoTag(self):
        parent = ParentNode(tag=None, children=[], props={"class": "parent"})
        with self.assertRaises(ValueError):
            parent.to_html()
if __name__ == "__main__":
    unittest.main()
