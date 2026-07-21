import unittest
from delimiters import splitNodeDelimiter
from textnode import TextNode, TextType


class TestDelimiter(unittest.TestCase):
    def test_basic_working(self):
        node= TextNode("this is a sample text that has an `code` block inside of it", TextType.TEXT)
        newNodeList = splitNodeDelimiter([node], "`", TextType.CODE)
        expected = [TextNode("this is a sample text that has an ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" block inside of it", TextType.TEXT)]
        self.assertEqual(newNodeList, expected)

    def test_valueError(self):
        node= TextNode("this is a text that is used to `break logic intentionally", TextType.TEXT)
        with self.assertRaises(ValueError):
            newNodeList = splitNodeDelimiter([node],"`", TextType.CODE)

    def test_with_two_different_delimiters(self):
        node= TextNode("this is `code` and the next line is also `code` so you can make me sit next to britney spearks", TextType.TEXT)
        newNodeList = splitNodeDelimiter([node],"`",TextType.CODE)
        for newNodes in newNodeList:
            if newNodes.text_type == TextType.CODE:
                self.assertEqual(newNodes.text,"code")

    def test_basic_working_again(self):
        node= TextNode("this is a sample text that has an **BOLD** block inside of it", TextType.TEXT)
        newNodeList = splitNodeDelimiter([node], "**", TextType.BOLD)
        expected = [TextNode("this is a sample text that has an ", TextType.TEXT), TextNode("BOLD", TextType.BOLD), TextNode(" block inside of it", TextType.TEXT)]
        self.assertEqual(newNodeList, expected)

if __name__ == "__main__":
    unittest.main()