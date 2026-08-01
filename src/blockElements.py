from enum import Enum
import re


def markdown_to_blocks(text):
    processedBlocks=[]
    extractedBlocks = text.split("\n\n")
    for block in extractedBlocks:
        lines = block.split("\n")

        stripedLine = [line.strip() for line in lines]
        cleanedBlock = "\n".join(stripedLine).strip()

        if cleanedBlock:
            processedBlocks.append(cleanedBlock)


    # print(processedBlocks)
    return processedBlocks


class BlockType(Enum):
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    PARAGRAPH = "paragraph"

def block_to_blockType(block):
    print(block)
    print("i guess nothing ")
    typeHeading = re.findall(r"^#{1,6}\s+.*$", block)
    if typeHeading:
        return BlockType.HEADING
    typeCode = re.findall(r"```$", block)
    if typeCode:
        return BlockType.CODE
    typeQuote = re.findall(r">.*$", block)
    if typeQuote:
        return BlockType.QUOTE
    typeUnorderedList = re.findall(r"- .*$", block)
    if typeUnorderedList:
        return BlockType.UNORDERED_LIST
    typeOrderedList = re.findall(r"\d+\. .*$", block)
    if typeOrderedList:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def main():
    a=block_to_blockType(" 6. hello world")
    print(a)
    
    # def main():
    #     print("this is the main function")
    #     md = """This is **bolded** paragraph
main()
#     This is another paragraph with _italic_ text and `code` here
#     This is the same paragraph on a new line

#     - This is a list
#     - with items
#     """
#     blocks = markdown_to_blocks(md)
#     print(blocks)
#     print(f"and the length is {len(blocks)}")


# main()
