import unittest
from main import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextnodes(unittest.TestCase):
    def test_basic_working(self):
        obtainedCoversion =text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        expectedTextnode= [TextNode("This is ", TextType.TEXT, None), TextNode("text", TextType.BOLD, None), TextNode(" with an ", TextType.TEXT, None), TextNode("italic", TextType.ITALIC, None), TextNode(" word and a ", TextType.TEXT, None), TextNode("code block", TextType.CODE, None), TextNode(" and an ", TextType.TEXT, None), TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode(" and a ", TextType.TEXT, None), TextNode("link", TextType.LINK, "https://boot.dev")]
        # self.assertListEqual(expectedTextnode ,a)
            
        self.assertListEqual(expectedTextnode, obtainedCoversion)
        
    def test_noClosing_tag_conversion(self):
        with self.assertRaises(ValueError):
            text_to_textnodes("this will not make sense `` * ** __ * are these enough nah lets do more `` ** -_ _")
    
    def test_lets_do_oneWith_empty_tags(self):
        obtainedConversion = text_to_textnodes(" ** ** ` `") 
        expectedResponse = [
            TextNode(" ",TextType.TEXT),
            TextNode(" ",TextType.BOLD),
            TextNode(" ",TextType.TEXT),
            TextNode(" ",TextType.CODE)
        ]
        self.assertEqual(expectedResponse,obtainedConversion)
        
    def test_check_valueError_for_delimiter_layering(self):
        with self.assertRaises(ValueError):
            text_to_textnodes("**``**")
