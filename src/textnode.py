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

def main():
    node = TextNode("Hello world", TextType.PLAIN, None)
    print(node)

main()

# def main():
#     node = TextNode("Hello, world!", TextType.PLAIN_TEXT)
#     print(node)

#reate a main() function in main.py and call it. The function should create a new TextNode object with some dummy values. Print the object, and make sure it looks like you'd expect. For example, my code printed: