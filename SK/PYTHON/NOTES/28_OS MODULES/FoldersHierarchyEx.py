# 2. create a Folder Hierarchy
#FoldersHierarchyEx.py
import os
try:
    os.makedirs("C:\\INDIA\\TS\\HYD\\PYTHON")
    print("Folders Hierarchy Created--verify")
except FileExistsError:
    print("Folders Hierarchy already exist")