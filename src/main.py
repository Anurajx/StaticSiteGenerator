from textnode import TextNode, TextType
from regex import splitNodeImage, splitNodeLink
from delimiters import splitNodeDelimiter

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
    a=text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
    print(a)
main()