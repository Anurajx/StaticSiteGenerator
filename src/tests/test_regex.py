import unittest
from regexExtract import extract_markdown_image, extract_markdown_link, splitNodeImage, splitNodeLink
from textnode import TextNode, TextType


class TestRegex(unittest.TestCase):
    def test_extract_markdown_image(self):
        matches = extract_markdown_image(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        #add more tests for regex Link and Texts

    def test_extract_multiple_markdown_image(self):
        matches = extract_markdown_image(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and once again ![image](https://i.imgur.com/zjjcJKZ.png) okay that's enough"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_markdown_link(self):
        matches = extract_markdown_link("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_extract_image_with_noAlt(self):
        matches = extract_markdown_image(
            "This is text with an ![](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_image_noInfo(self):
        matches = extract_markdown_image(
            "This is text with an ![]()"
        )
        self.assertListEqual([("", "")], matches)

    def test_extract_link_noInfo(self):
        matches = extract_markdown_link(
            "This is text with an []()"
        )
        self.assertListEqual([("", "")], matches)

    def test_link_with_image_url(self):
        matches = extract_markdown_link("wassup bud ![is this the redpill world](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([], matches) #makes sure image are not read as link


    def test_extract_with_no_image(self):
        matches = extract_markdown_image("dosa tops burger pizza is comparable")
        self.assertListEqual([],matches)

    # def test_linkNode_extraction(self):
    #     node= TextNode("wassup bud [is this the redpill world link](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
    #     newNodeList = splitNodeLink([node])
    #     print(newNodeList)
    #     expected = "[TextNode(wassup bud , TextType.TEXT, None), TextNode(is this the redpill world link, TextType.LINK, https://i.imgur.com/zjjcJKZ.png)]"
    #     self.assertEqual(newNodeList, expected)

    def test_split_link(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = splitNodeLink([node])
        self.assertEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = splitNodeImage([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_empty_image(self):
        node = TextNode("this is a test with empty image tags ![]() i guess thats enough but why not test with an empty link node []() good? ",TextType.TEXT)
        new_nodes= splitNodeImage([node])
        self.assertListEqual(
            [
                TextNode("this is a test with empty image tags ", TextType.TEXT),
                TextNode("",TextType.IMAGE,""),
                TextNode(" i guess thats enough but why not test with an empty link node []() good? ", TextType.TEXT)
            ],
            new_nodes
        )

    def test_split_empty_link(self):
        node = TextNode("this is a test with empty image tags []() i guess thats enough but why not test with an empty link node ![]() good? ",TextType.TEXT)
        new_nodes= splitNodeLink([node])
        self.assertListEqual(
            [
                TextNode("this is a test with empty image tags ", TextType.TEXT),
                TextNode("",TextType.LINK,""),
                TextNode(" i guess thats enough but why not test with an empty link node ![]() good? ", TextType.TEXT)
            ],
            new_nodes
        )

    def test_split_empty_link_only(self):
        node = TextNode("[]() []()(())", TextType.TEXT)
        new_nodes=splitNodeLink([node])
        self.assertListEqual(
            [
                TextNode("", TextType.LINK,""),
                TextNode(" ",TextType.TEXT),
                TextNode("", TextType.LINK,""),
                TextNode("(())", TextType.TEXT)
            ],
            new_nodes
        )
