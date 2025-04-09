#FileOpenEx7.py
try:
    with open("stud1.data","x") as fp:
            print("-------------------------------------")
            print("File Opened in Exclusive Write Mode Sucessfilly")
            print("Type of fp=",type(fp)) # <class '_io.TextIOWrapper'>
            print("-------------------------------------")
            print("Name of the File=", fp.name)
            print("File Mode=", fp.mode)
            print("is File Redable?=", fp.readable())
            print("is File Writable?=", fp.writable())
            print("is File closed?=", fp.closed)
            print("-------------------------------------")
    print("is File closed after with open() as ?=", fp.closed)
except FileExistsError:
    print("File already exist")
