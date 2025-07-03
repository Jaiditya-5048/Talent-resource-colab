#RenameFolder.py
import os
try:
    os.rename("C:\\RS","C:\\ROSSUM")
    print("Folder Renamed--verify")
except FileNotFoundError:
    print("Folder Does not Exist")