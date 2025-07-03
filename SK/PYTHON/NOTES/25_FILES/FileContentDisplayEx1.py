#Program for Displaying the content of any file
#FileContentDisplayEx1.py
try:
    filename=input("Enter File Name: to view its content:")
    with open(filename,"r") as fp:
        filedata=fp.read()
        print("---------------------------------------------")
        print("Content of {}".format(fp.name))
        print("---------------------------------------------")
        print(filedata)
        print("---------------------------------------------")
except FileNotFoundError:
    print("File does not exist:")