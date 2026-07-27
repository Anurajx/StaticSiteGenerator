import re
from textnode import TextNode, TextType

def extract_markdown_image(text):
    matchedSubsection = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return matchedSubsection

def extract_markdown_link(text):
    matchedSubsection = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)
    return matchedSubsection


#implementing actuall extractions logic
def splitNodeImage(old_nodes: [TextNode]) -> list[TextNode]:
    newNodes=[]
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            newNodes.append(node)
            continue

        extractedImage= extract_markdown_image(node.text)
        #print(extractedImage)
        

        if len(extractedImage)==0:
            newNodes.append(node)
            continue


        remainingNode= node.text
        for alt, url in extractedImage:
            firstRemainingSideNode, remainingNode= remainingNode.split(f"![{alt}]({url})",1)
            #print("THESE ARE THE REMAINING NODES")
            #print(firstRemainingSideNode)
            #print(remainingNode)
            if firstRemainingSideNode:
                newNodes.append(TextNode(firstRemainingSideNode, TextType.TEXT))
            newNodes.append(TextNode(alt, TextType.IMAGE, url))
        if remainingNode:
            newNodes.append(TextNode(remainingNode, TextType.TEXT))


    return newNodes


def splitNodeLink(old_nodes: [TextNode]) -> list[TextNode]:
    newNodes=[]
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            newNodes.append(node)
            continue
        

        extractedLink= extract_markdown_link(node.text)
        #print(extractedLink)
        

        if len(extractedLink)==0:
            # print(f"SKIPPING EXTRACTION-- {extractedLink} FOR {old_nodes}")
            newNodes.append(node)
            continue

        remainingNode= node.text
        for alt, url in extractedLink:
            firstRemainingSideNode, remainingNode= remainingNode.split(f"[{alt}]({url})",1)
            #print("THESE ARE THE REMAINING NODES")
            #print(firstRemainingSideNode)
            #print(remainingNode)

            if firstRemainingSideNode:
                newNodes.append(TextNode(firstRemainingSideNode, TextType.TEXT))


            newNodes.append(TextNode(alt, TextType.LINK, url))
        if remainingNode:
            newNodes.append(TextNode(remainingNode, TextType.TEXT))

        # for i in extractedLink:
        #     print(i)
        #     # sideExtractedNodes= node.text.split(i,1)
        #     newNodes.append(i)



        #newNodes.append(extractedLink)

    return newNodes

def main():
    # testingMicImage= "hey why are there so many link (outthere) shoudnt ![rick roll](https://i.imgur.com/aKaOqIh.gif) they be (inside) there homes at this ![rick roll](https://i.imgur.com/aKaOqIh.gif) time, link hut"
    # testingMicText=  "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # t=extract_markdown_image(testingMicImage)
    # a=extract_markdown_link(testingMicText)
    node= TextNode("wassup bud [is this the redpill world link1](https://i.imgur.com/zjjcJKZ.png) once again bcs why not ", TextType.TEXT)
    newNodeList = splitNodeLink([node])
    # print(t)

    print(newNodeList)

# main()

