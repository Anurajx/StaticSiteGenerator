import os
import shutil
import pathlib
import re
from converterMDtoNodes import markdown_to_html_node

def extract_heading(markdown):
    heading = re.findall(r"^# (.*?)$", markdown, re.MULTILINE) 
    
    if not heading:
        raise Exception("There is no H1 heading in markdown")
    
    return heading[0].strip()
    
    
def generate_page(from_path, template_path, dest_path):
    #print(f"generating page from {from_path} to {dest_path} using {template_path}")
    
    f= open(from_path,"r") #reading Markdown
    extractedMarkdown = f.read()
    f.close()
    

    
    f=open(template_path,"r")
    extractedTemplate = f.read()
    f.close()
    
    convertedHTML = markdown_to_html_node(extractedMarkdown).to_html()
    websiteTitle = extract_heading(extractedMarkdown)
    
    firstConverstion= extractedTemplate.replace("{{ Title }}", websiteTitle)
    secondConversion = firstConverstion.replace("{{ Content }}", convertedHTML)
    
    HTMLfilePath= os.path.join(dest_path, "index.html")
    f=open(HTMLfilePath,"w")
    f.write(secondConversion)
    f.close()
    
    
def generate_page_recursively(content_dir, template_path, public_dir):
    for item in os.listdir(content_dir):
        content_path = os.path.join(content_dir, item)

        if os.path.isdir(content_path):
            public_subdir = os.path.join(public_dir, item)
            os.makedirs(public_subdir, exist_ok=True)

            generate_page_recursively(
                content_path,
                template_path,
                public_subdir
            )

        elif item.endswith(".md"):
            name = os.path.splitext(item)[0]

            if name == "index":
                destination_dir = public_dir
            else:
                destination_dir = os.path.join(public_dir, name)

            os.makedirs(destination_dir, exist_ok=True)

            generate_page(
                content_path,
                template_path,
                destination_dir
            )    
# def generate_page_recursively(dir_path_content, template_path, dest_dir_path):
#     subDirList=os.listdir(dir_path_content)
#     for i in subDirList:
#         subDirectoryContentPath = os.path.join(dir_path_content,i)
#         #HTMLdestFilePath= os.path.join(dest_dir_path, "index.html")
#         HTMLdestFilePath= dest_dir_path
#         #print(i)
#         if os.path.isdir(subDirectoryContentPath):
#             os.mkdir(os.path.join(dest_dir_path,i))
#             HTMLdestFilePath= os.path.join(dest_dir_path, f"{HTMLdestFilePath}/index.html")
#             generate_page_recursively(subDirectoryContentPath, template_path, HTMLdestFilePath)
#             continue
            
#         f= open(subDirectoryContentPath,"r") #reading Markdown
#         extractedMarkdown = f.read()
#         f.close()
        
        
#         f=open(template_path,"r")
#         extractedTemplate = f.read()
#         f.close()
        
#         convertedHTML = markdown_to_html_node(extractedMarkdown).to_html()
#         websiteTitle = extract_heading(extractedMarkdown)
        
#         firstConverstion= extractedTemplate.replace("{{ Title }}", websiteTitle)
#         secondConversion = firstConverstion.replace("{{ Content }}", convertedHTML)
        
        

#         # HTMLdestFilePath= os.path.join(dest_dir_path, f"{i}/index.html")
#         print(f"hence the path is {HTMLdestFilePath}")
#         f=open(HTMLdestFilePath,"w")
#         f.write(secondConversion)
#         f.close()
    


def staticToPublicFileCopy():
    #print("Hello, World!")
    publicPath = pathlib.Path(__file__).parent.parent / "public"
    staticPath = pathlib.Path(__file__).parent.parent / "static"
    
    if(os.path.exists(publicPath) and os.path.isdir(publicPath)):
        #print(os.listdir(publicPath))
        shutil.rmtree(publicPath)
        os.makedirs(publicPath)
    if(os.path.exists(staticPath) and os.path.isdir(staticPath)):
        recursiveCopy(staticPath,publicPath)
        # shutil.copytree(staticPath, publicPath, dirs_exist_ok=True)  #this would also work just without logging file change
    #print(f"Deleting public folder at: {publicPath}, and static folder at: {staticPath}")

def recursiveCopy(src, dest):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        
        if os.path.isdir(s):
            os.mkdir(d)
            recursiveCopy(s,d)
        else:
            shutil.copy(s,d)
            #print(f"MOVED {s} ---> {d}")
            
            

def main():
    staticToPublicFileCopy()
    publicPath = pathlib.Path(__file__).parent.parent / "public"
    contentPath = pathlib.Path(__file__).parent.parent / "content"
    parentPath = pathlib.Path(__file__).parent.parent
    
    
    templatePath= os.path.join(parentPath, "template.html")
    #markdownPath = os.path.join(contentPath, "index.md")
    
    
    print(f"before hand {publicPath}")
    generate_page_recursively(contentPath, templatePath, publicPath)
    #first is markdown - content/index.md
    #second is template.html
    #third is public
    
    # if os.path.isfile(markdownPath):
    #     print(f"SUCCESS {markdownPath}")
        
    #generate_page(markdownPath, templatePath, publicPath)
    
main()