class HTMLNode:
    def __init__(self=None, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented for base HTMLNode class")

    def props_to_html(self):
        if not self.props:
            return ""
        finalProp = " ".join([f'{key}="{value}"' for key, value in self.props.items()])
        return finalProp

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=[], props=props)

    def to_html(self):
        props_str = self.props_to_html()
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        if self.tag == "img":
            return f'<{self.tag} {props_str}>' #special case for img since closing tag is not needed

        return f"<{self.tag} {props_str}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"

    
class ParentNode(HTMLNode):
    def __init__(self, tag, children=None, props=None):
        super().__init__(tag=tag, value=None, children=children or None, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("Parent Node must have atleast one child")
            

        props_str = self.props_to_html()
        children_html = " ".join([child.to_html() for child in self.children]) #recursively calling to_html on each child node
        return f"<{self.tag} {props_str}>{children_html}</{self.tag}>"



def main():
    node = HTMLNode(tag="div", value="Hello world", children=[], props={"class": "my-class", "id": "my-id"})
    print(node.props_to_html())
    print("hello")

if __name__ == "__main__":
    main()