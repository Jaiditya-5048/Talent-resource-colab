#Program for Reading the Data from the File
#FileReadEx2.py
try:
    with open("E:\\KVR-PYTHON-11AM\\FILES\\NOTES\\hyd.info") as fp:
        filedata=fp.readlines()
        for record in filedata:
            print(record,end="")
except FileNotFoundError:
    print("File Does not Exist")