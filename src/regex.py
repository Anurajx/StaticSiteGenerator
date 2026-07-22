import re

def extract_markdown_images(text):
    matchedSubsection = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return matchedSubsection

def extract_markdown_links(text):
    matchedSubsection = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)
    return matchedSubsection


def main():
    testingMicImages= "hey why are there so many links (outthere) shoudnt ![rick roll](https://i.imgur.com/aKaOqIh.gif) they be (inside) there homes at this ![rick roll](https://i.imgur.com/aKaOqIh.gif) time, links hut"
    testingMicText=  "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    extract_markdown_images(testingMicImages)
    extract_markdown_links(testingMicText)

# main()