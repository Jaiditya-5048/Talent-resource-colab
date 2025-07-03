#FileOpenEx1.py
try:
    kvr=open("stud.data","r")
    print("File Opened in read mode")
except FileNotFoundError:
    print("File Does not Exist")