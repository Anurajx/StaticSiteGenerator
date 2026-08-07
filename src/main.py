from textnode import TextNode, TextType
from regexExtract import splitNodeImage, splitNodeLink
from delimiters import splitNodeDelimiter
from blockElements import markdown_to_blocks, block_to_blockType, BlockType
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import text_node_to_html_node


def markdown_to_html_node(markdown):
    #print("your time will come")
    processedBlocks = markdown_to_blocks(markdown)
    #print(f"processedBlocks: {processedBlocks}")
    children = []
    for block in processedBlocks:
        block_type = block_to_blockType(block)
        childs = block_to_html_node_helper(block, block_type)
        #print(f"CHILD    -  {childs}")
        children.append(childs)
    return ParentNode("div", children)

def block_to_html_node_helper(block, block_type):
    if block_type == BlockType.PARAGRAPH:
        block = block.replace("\n", " ")
        return ParentNode("p", [text_node_to_html_node(text_node) for text_node in text_to_textnodes(block)])
    elif block_type == BlockType.HEADING:
        return ParentNode("h1", [text_node_to_html_node(text_node) for text_node in text_to_textnodes(block)])
    
    elif block_type == BlockType.QUOTE:
        return ParentNode("blockquote", [text_node_to_html_node(text_node) for text_node in text_to_textnodes(block)])
    
    elif block_type == BlockType.CODE: #For ``` cases 
        return ParentNode("pre", [LeafNode("code", block.strip("```"))])
    
    elif block_type == BlockType.UNORDERED_LIST:
        block = block.split("\n")
        list_items = []
        for item in block:
            list_items.append(LeafNode("li", item))
        return ParentNode("ul", list_items)
    
    elif block_type == BlockType.ORDERED_LIST:
        block = block.split("\n")
        list_items = []
        for item in block:
            list_items.append(LeafNode("li", item))
        return ParentNode("ol", list_items)
        
        
        
        


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




# def main():
#     md = """
#                     This is **bolded** paragraph

#                     This is another paragraph with _italic_ text and `code here`
#                     This is the same paragraph on a new line wassup bud [is this the redpill world link1](https://i.imgur.com/zjjcJKZ.png) once again bcs why not 

#                     - This is a list
#                     - with items
                    
                    
#                     """
#     blocks = markdown_to_html_node(md)
#     # a=text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
#     # print(a)
# main()
