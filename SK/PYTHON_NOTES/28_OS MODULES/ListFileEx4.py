#ListFileEx4.py
import os
try:
    FolderName=input("Enter the Folder Name to list the files:")
    FileList=os.listdir(FolderName)
    print("-------------------------------------")
    print("Total Number Files=",len(FileList))
    for filename in FileList[::-1]:
        if(filename.endswith(".py")):
            print("\t{}".format(filename))
    print("-------------------------------------")

except FileNotFoundError:
    print("Folder does not exist")