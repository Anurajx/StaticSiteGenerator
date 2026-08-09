import unittest
from converterMDtoNodes import text_to_textnodes, markdown_to_html_node, block_to_blockType, block_to_html_node_helper
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
            
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(html)
        self.assertEqual(
            html,
            "<div ><p >This is <b >bolded</b> paragraph\n    text in a p\n    tag here</p><p >This is another paragraph with <i >italic</i> text and <code >code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(html)
        self.assertEqual(
            html,
            #"<div ><pre ><code >This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
            "<div ><pre ><code >    This is text that _should_ remain\n    the **same** even with inline stuff</code></pre></div>",
        )
