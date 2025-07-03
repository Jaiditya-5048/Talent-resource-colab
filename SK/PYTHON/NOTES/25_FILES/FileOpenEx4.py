#FileOpenEx4.py
try:
    fp=open("stud.data","r")
except FileNotFoundError:
    print("File does not Exist")
else:
    print("-------------------------------------")
    print("File Opened in read Mode Sucessfilly")
    print("Type of fp=", type(fp))  # <class '_io.TextIOWrapper'>
    print("-------------------------------------")
    print("Name of the File=", fp.name)
    print("File Mode=", fp.mode)
    print("is File Redable?=", fp.readable())
    print("is File Writable?=", fp.writable())
    print("is File closed?=", fp.closed)
    print("-------------------------------------")
finally:
    print("I am from finally block")
    print("is File closed in finally block?=", fp.closed)
    fp.close()
    print("is File closed in after manual close?=", fp.closed)
