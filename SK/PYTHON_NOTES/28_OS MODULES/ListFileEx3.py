#ListFileEx3.py
import os
try:
    FileList=os.listdir("E:\\KVR-PYTHON-11AM\\FILES")
    print("-------------------------------------")
    print("Total Number Files=",len(FileList))
    nop=0
    for filename in FileList:
        if(filename[-3:]==".py"):
            nop=nop+1
            print("\t{}".format(filename))
    print("-------------------------------------")
    print("Number of Python Files=",nop)
except FileNotFoundError:
    print("Folder does not exist")