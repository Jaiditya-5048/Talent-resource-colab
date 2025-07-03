#RenameFileName.py
import os
try:
    os.rename("kvr.py","sample.py")
    print("File Renamed--verify")
except FileNotFoundError:
    print("File Name does not exist")