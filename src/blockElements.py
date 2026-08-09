from enum import Enum
import re


def markdown_to_blocks(text):
    processedBlocks=[]
    extractedBlocks = text.split("\n\n")
    for block in extractedBlocks:
        lines = block.split("\n")

        Line = [line for line in lines]
        cleanedBlock = "\n".join(Line).strip()

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
    
    if re.match(r"^#{1,6} .+$", block):
        return BlockType.HEADING
    
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    subParts = block.split("\n")
    if all(line.startswith(">") for line in subParts):
        return BlockType.QUOTE
    
    if all(line.startswith("-") for line in subParts):
        return BlockType.UNORDERED_LIST
    
    for i, line in enumerate(subParts, start=1):
        if not line.startswith(fr"{i}. "):
            break
        else:
            return BlockType.ORDERED_LIST
        
    
    return BlockType.PARAGRAPH

# def main():
#     a=block_to_blockType("""1. hello 
# 2. world""")
#     print(a)
    
#     # def main():
#     #     print("this is the main function")
#     #     md = """This is **bolded** paragraph
# main()
#     This is another paragraph with _italic_ text and `code` here
#     This is the same paragraph on a new line

#     - This is a list
#     - with items
#     """
#     blocks = markdown_to_blocks(md)
#     print(blocks)
#     print(f"and the length is {len(blocks)}")


# main()
