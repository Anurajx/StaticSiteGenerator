import unittest
from regex import extract_markdown_images, extract_markdown_links


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

