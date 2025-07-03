#ListFileEx1.py
import os
try:
    FileList=os.listdir("E:\\KVR-PYTHON-11AM\\FILES")
    print("-------------------------------------")
    for filename in FileList:
        print("\t{}".format(filename))
    print("-------------------------------------")
except FileNotFoundError:
    print("Folder does not exist")