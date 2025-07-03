# 1. create a Folder--os.mkdir("FolderName")
#CreateFolderEx.py
import os
try:
    os.mkdir("PYTHONPROG\\HYD")
    print("Folder Created--Verify")
except FileExistsError:
    print("Folder already created")
except FileNotFoundError:
    print("Root Folder Does not Exit")
