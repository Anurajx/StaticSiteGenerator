import os
import shutil
import pathlib
import re

def extract_heading(markdown):
    heading = re.findall(r"^# (.*?)$", markdown, re.MULTILINE) 
    
    if not heading:
        raise Exception("There is no H1 heading in markdown")
    
    return heading[0].strip()
    
    

















def staticToPublicFileCopy():
    #print("Hello, World!")
    publicPath = pathlib.Path(__file__).parent.parent / "public"
    staticPath = pathlib.Path(__file__).parent.parent / "static"
    
    if(os.path.exists(publicPath) and os.path.isdir(publicPath)):
        # print(os.listdir(publicPath))
        # print(f"Deleting public folder at: {publicPath}")
        shutil.rmtree(publicPath)
        os.makedirs(publicPath)
    if(os.path.exists(staticPath) and os.path.isdir(staticPath)):
        #print(os.listdir(staticPath))
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
    
main()