import unittest
from regex import extract_markdown_images, extract_markdown_links, splitNodeImage, splitNodeLink
from textnode import TextNode, TextType


class TestRegex(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        #add more tests for regex Links and Texts

    def test_extract_multiple_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and once again ![image](https://i.imgur.com/zjjcJKZ.png) okay that's enough"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_multiple_markdown_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_extract_images_with_noAlt(self):
        matches = extract_markdown_images(
            "This is text with an ![](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_images_noInfo(self):
        matches = extract_markdown_images(
            "This is text with an ![]()"
        )
        self.assertListEqual([("", "")], matches)

    def test_extract_links_noInfo(self):
        matches = extract_markdown_links(
            "This is text with an []()"
        )
        self.assertListEqual([("", "")], matches)

    def test_links_with_image_url(self):
        matches = extract_markdown_links("wassup bud ![is this the redpill world](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([], matches) #makes sure images are not read as links


    def test_extract_with_no_images(self):
        matches = extract_markdown_images("dosa tops burger pizza is comparable")
        self.assertListEqual([],matches)

    # def test_linkNode_extraction(self):
    #     node= TextNode("wassup bud [is this the redpill world link](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
    #     newNodeList = splitNodeLink([node])
    #     print(newNodeList)
    #     expected = "[TextNode(wassup bud , TextType.TEXT, None), TextNode(is this the redpill world link, TextType.LINKS, https://i.imgur.com/zjjcJKZ.png)]"
    #     self.assertEqual(newNodeList, expected)

    def test_split_links(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = splitNodeLink([node])
        self.assertEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINKS, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.LINKS, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = splitNodeImage([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_empty_images(self):
        node = TextNode("this is a test with empty image tags ![]() i guess thats enough but why not test with an empty link node []() good? ",TextType.TEXT)
        new_nodes= splitNodeImage([node])
        self.assertListEqual(
            [
                TextNode("this is a test with empty image tags ", TextType.TEXT),
                TextNode("",TextType.IMAGES,""),
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
                TextNode("",TextType.LINKS,""),
                TextNode(" i guess thats enough but why not test with an empty link node ![]() good? ", TextType.TEXT)
            ],
            new_nodes
        )

    def test_split_empty_links_only(self):
        node = TextNode("[]() []()(())", TextType.TEXT)
        new_nodes=splitNodeLink([node])
        self.assertListEqual(
            [
                TextNode("", TextType.LINKS,""),
                TextNode(" ",TextType.TEXT),
                TextNode("", TextType.LINKS,""),
                TextNode("(())", TextType.TEXT)
            ],
            new_nodes
        )


    
