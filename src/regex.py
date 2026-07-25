import re
from textnode import TextNode, TextType

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
        if node.text_type != TextType.TEXT:
            newNodes.append(node)

        extractedImages= extract_markdown_images(node.text)
        

        if len(extractedImages)==0:
            newNodes.append(node)
        for alt, url in extractedImages:
            newNodes.append(TextNode(alt, TextType.IMAGES, url))
        # for i in extractedImages:
        #     print(i)
        #     newNodes.append(i)

        #newNodes.append(extractedImages)

    return newNodes


def splitNodeLink(old_nodes: [TextNode]) -> list[TextNode]:
    newNodes=[]
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            newNodes.append(node)
            continue
        

        extractedLinks= extract_markdown_links(node.text)
        print(extractedLinks)
        

        if len(extractedLinks)==0:
            newNodes.append(node)
            continue

        remainingNode= node.text
        for alt, url in extractedLinks:
            firstRemainingSideNode, remainingNode= remainingNode.split(f"[{alt}]({url})",1)
            print("THESE ARE THE REMAINING NODES")
            #print(firstRemainingSideNode)
            print(remainingNode)

            if firstRemainingSideNode:
                newNodes.append(TextNode(firstRemainingSideNode, TextType.TEXT))


            newNodes.append(TextNode(alt, TextType.LINKS, url))
        if remainingNode:
            newNodes.append(TextNode(remainingNode, TextType.TEXT))

        # for i in extractedLinks:
        #     print(i)
        #     # sideExtractedNodes= node.text.split(i,1)
        #     newNodes.append(i)



        #newNodes.append(extractedLinks)

    return newNodes

def main():
    # testingMicImages= "hey why are there so many links (outthere) shoudnt ![rick roll](https://i.imgur.com/aKaOqIh.gif) they be (inside) there homes at this ![rick roll](https://i.imgur.com/aKaOqIh.gif) time, links hut"
    # testingMicText=  "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # t=extract_markdown_images(testingMicImages)
    # a=extract_markdown_links(testingMicText)
    node= TextNode("wassup bud [is this the redpill world link1](https://i.imgur.com/zjjcJKZ.png) once again bcs why not ", TextType.TEXT)
    newNodeList = splitNodeLink([node])
    # print(t)

    print(newNodeList)

# main()

