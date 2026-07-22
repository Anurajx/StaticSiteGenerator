from textnode import TextNode, TextType


def splitNodeDelimiter(old_nodes: [TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    
    
    
    newNode = []
    #print(node)
    for node in old_nodes:
        if node.text_type != TextType.TEXT: #Only performs splitting if the text type is raw text
            newNode.append(node)
            continue

        section = node.text.split(delimiter) #text is extracted as section

        if len(section) % 2 == 0:
            raise ValueError("There is no closing delimiter -- {delimiter}")
        
        for i, section in enumerate(section):
            if section == "":
                continue
            if i % 2 == 0:
                newNode.append(TextNode(section, TextType.TEXT))
            else:
                newNode.append(TextNode(section, text_type))
    return newNode

def splitNodeImage(old_nodes: [TextNode]) -> list[TextNode]:
    print("complete this tmrw")

def splitNodeLink(old_nodes: [TextNode]) -> list[TextNode]:
    print("and this too")



def main():
    print("holdup boy dads cookin")
    node = TextNode("This is text block with a `code block` inside of it", TextType.TEXT)
    new_node= splitNodeDelimiter([node], "`", TextType.CODE)