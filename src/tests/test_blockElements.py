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
            
            
class TestBlocktoBlockTypeConversion(unittest.TestCase):
    def test_block_to_blockType(self):
        self.assertEqual(block_to_blockType("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_blockType("```\nCode block\n```"), BlockType.CODE)
        self.assertEqual(block_to_blockType("> Quote"), BlockType.QUOTE)
        self.assertEqual(block_to_blockType("- Unordered list item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_blockType("1. Ordered list item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_blockType("This is a paragraph."), BlockType.PARAGRAPH)
        
    def test_complex_block_to_blockType(self):
        self.assertEqual(block_to_blockType("> Quote\n> Another line of quote"), BlockType.QUOTE)
        self.assertEqual(block_to_blockType("- Item 1\n- Item 2\n- Item 3"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_blockType("1. First item\n2. Second item\n3. Third item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_blockType("This is a paragraph with multiple lines.\nThis is the second line of the paragraph."), BlockType.PARAGRAPH)
        