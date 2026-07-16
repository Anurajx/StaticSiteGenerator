from enum import Enum

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "link"
    IMAGES = "image"

class TextNode(object):
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if(self.text == other.text and self.text_type == other.text_type and self.url == other.url):
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


    def text_node_to_html_node(text_node: TextNode) -> LeafNode: #the thing in front of arrow indicates the return type, although python does not enforce it. TextNode is the argument type
        if text_node.text_type == TextType.PLAIN: # the thing in front of text_node is the object, and the thing after the dot is the attribute of that object
            return LeafNode(text_node.text, "p")
        elif text_node.text_type == TextType.BOLD:
            return LeafNode(text_node.text, "b")
        elif text_node.text_type == TextType.ITALIC:
            return LeafNode(text_node.text, "i")
        elif text_node.text_type == TextType.CODE:
            return LeafNode(text_node.text, "code")
        elif text_node.text_type == TextType.LINKS:
            return LeafNode(text_node.text, "a", {"href": text_node.url})
        elif text_node.text_type == TextType.IMAGES:
            return LeafNode(text_node.text, "img",{"src": text_node.url})
        else:
            raise ValueError("Invalid text type")


def main():
    node = TextNode("Hello world", TextType.PLAIN, None)
    print(node)

main()

# def main():
#     node = TextNode("Hello, world!", TextType.PLAIN_TEXT)
#     print(node)

#reate a main() function in main.py and call it. The function should create a new TextNode object with some dummy values. Print the object, and make sure it looks like you'd expect. For example, my code printed: