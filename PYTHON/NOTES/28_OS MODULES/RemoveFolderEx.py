#RemoveFolderEx.py
import os
try:
    os.rmdir("C:\\tr")
    print("Folder Removed--verify")
except FileNotFoundError:
    print("Folder Does not Exist")
except OSError:
    print("Folder Contains File(s)-make sure that folder must be empty")