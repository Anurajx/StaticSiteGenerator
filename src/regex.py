import re
from textnode import TextNode

def extract_markdown_images(text):
    matchedSubsection = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return matchedSubsection

def extract_markdown_links(text):
    matchedSubsection = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)
    return matchedSubsection


#implementing actuall extractions logic
def splitNodeImage(old_nodes: [TextNode]) -> list[TextNode]:
    newNodes=[]
    for node in old_nodes:
        extractedImages= extract_markdown_images(node.text)
        newNodes.append(extractedImages)
    print("complete this tmrw")
    return newNodes

def splitNodeLink(old_nodes: [TextNode]) -> list[TextNode]:
    newNodes=[]
    for node in old_nodes:
        extractedLinks= extract_markdown_links(node.text)
        newNodes.append(extractedLinks)
    print("complete this tmrw")
    return newNodes

def main():
    testingMicImages= "hey why are there so many links (outthere) shoudnt ![rick roll](https://i.imgur.com/aKaOqIh.gif) they be (inside) there homes at this ![rick roll](https://i.imgur.com/aKaOqIh.gif) time, links hut"
    testingMicText=  "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    extract_markdown_images(testingMicImages)
    extract_markdown_links(testingMicText)

# main()