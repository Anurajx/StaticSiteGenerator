from textnode import TextNode, TextType
from regexExtract import splitNodeImage, splitNodeLink
from delimiters import splitNodeDelimiter
from blockElements import markdown_to_blocks, block_to_blockType, BlockType


def markdown_to_html_node(markdown):
    print("your time will come")
    processedBlocks = markdown_to_blocks(markdown)
    print(f"processedBlocks: {processedBlocks}")
    for block in processedBlocks:
        blockType = block_to_blockType(block)
        print(f"block: {block} block type: {blockType}")
        
        
    
    

def text_to_textnodes(text): #AGGREGATOR
    testNode= TextNode(text, TextType.TEXT)
    #print(f"TESTNODE MADE- {testNode}")
    testNode= splitNodeDelimiter([testNode],"`", TextType.CODE)
    #print(f"TESTNODE MADE- {testNode}")
    testNode= splitNodeDelimiter(testNode,"**", TextType.BOLD)
    #print(f"TESTNODE MADE- {testNode}")
    testNode= splitNodeDelimiter(testNode,"_", TextType.ITALIC)
    #print(f"TESTNODE MADE- {testNode}")
    testNode= splitNodeImage(testNode)
    #print(f"TESTNODE MADE- {testNode}")
    testNode= splitNodeLink(testNode)

    return testNode




def main():
    md = """
                    This is **bolded paragraph

                    This is another paragraph with _italic_ text and `code here`
                    This is the same paragraph on a new line

                    - This is a list
                    - with items
                    """
    blocks = markdown_to_html_node(md)
    # a=text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
    # print(a)
main()
