import os
import shutil
import pathlib
import re
import sys
from converterMDtoNodes import markdown_to_html_node





def extract_heading(markdown):
    heading = re.findall(r"^# (.*?)$", markdown, re.MULTILINE) 
    
    if not heading:
        raise Exception("There is no H1 heading in markdown")
    
    return heading[0].strip()
    
    
def generate_page(from_path, template_path, dest_path, basePath):# NOT CURRENTLY USED
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
    



def generate_page_recursively(dir_path_content, template_path, dest_dir_path, basePath):
    
    subDirList=os.listdir(dir_path_content)
    for i in subDirList:
        subDirectoryContentPath = os.path.join(dir_path_content,i)
        if os.path.isdir(subDirectoryContentPath):
            destFolderToCreate = os.path.join(dest_dir_path,i)
            os.mkdir(destFolderToCreate)
            generate_page_recursively(subDirectoryContentPath, template_path, destFolderToCreate, basePath)
            continue
        
        # if os.path.isdir(subDirectoryContentPath):
        #     print("FOLDERRRR COMING THROUGH")
        f= open(subDirectoryContentPath,"r") #reading Markdown
        extractedMarkdown = f.read()
        f.close()
        
        
        f=open(template_path,"r")
        extractedTemplate = f.read()
        f.close()
        
        convertedHTML = markdown_to_html_node(extractedMarkdown).to_html()
        websiteTitle = extract_heading(extractedMarkdown)
        
        firstConverstion = extractedTemplate.replace("{{ Title }}", websiteTitle)
        secondConversion = firstConverstion.replace("{{ Content }}", convertedHTML)
        thirdConversion = secondConversion.replace("""href="/""", f"""href="{basePath}""")
        fourthConversion = thirdConversion.replace("""src="/""", f"""src="{basePath}""")
        
        
        HTMLfilePath= os.path.join(dest_dir_path, "index.html")
        f=open(HTMLfilePath,"w")
        f.write(secondConversion)
        f.close()
    


def staticToPublicFileCopy():
    #print("Hello, World!")
    publicPath = pathlib.Path(__file__).parent.parent / "docs" #prev public
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
    publicPath = pathlib.Path(__file__).parent.parent / "docs" #prev public
    contentPath = pathlib.Path(__file__).parent.parent / "content"
    parentPath = pathlib.Path(__file__).parent.parent
    
    
    basePath= sys.argv[0]
    if not basePath:
        basePath="/"
    print(basePath)
    
    templatePath= os.path.join(parentPath, "template.html")
    generate_page_recursively(contentPath, templatePath, publicPath, basePath)
    


main()