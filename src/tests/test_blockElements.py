import unittest
from blockElements import markdown_to_blocks, block_to_blockType, BlockType

class TestMarkdownToBlockConversion(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
                    This is **bolded** paragraph

                    This is another paragraph with _italic_ text and `code` here
                    This is the same paragraph on a new line

                    - This is a list
                    - with items
                    """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
        )
            
            
           # ['This is **bolded** paragraph', '    This is another paragraph with _italic_ text and `code` here\n    This is the same paragraph on a new line', '    - This is a list\n    - with items\n    ']
        
        def test_markdown_with_no_closing_tag(self):
            md = """
                    This is **bolded paragraph

                    This is another paragraph with _italic_ text and `code here
                    This is the same paragraph on a new line

                    - This is a list
                    - with items
                    """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded paragraph",
                    "This is another paragraph with _italic_ text and `code here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
        )