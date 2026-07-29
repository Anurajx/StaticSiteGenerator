
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


# def main():
#     print("this is the main function")
#     md = """This is **bolded** paragraph

#     This is another paragraph with _italic_ text and `code` here
#     This is the same paragraph on a new line

#     - This is a list
#     - with items
#     """
#     blocks = markdown_to_blocks(md)
#     print(blocks)
#     print(f"and the length is {len(blocks)}")
    
    
# main()