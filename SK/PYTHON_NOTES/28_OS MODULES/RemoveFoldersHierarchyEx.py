#RemoveFoldersHierarchyEx.py
import os
try:
    os.removedirs("C:\\BANG")
    print("Folders Hierarchy Removed--verify")
except FileNotFoundError:
    print("Folders Hierarchy Does not Exist")
except OSError:
    print("Folders Contains File(s)-make sure that folder must be empty")