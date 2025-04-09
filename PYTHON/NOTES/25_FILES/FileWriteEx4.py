#Program for Writing the dynamic data to the file by reading from KBD
#FileWriteEx4.py
print("Enter the Data for writing to the file (Press @ to stop):")
with open("E:\\KVR-PYTHON-11AM\\FILES\\NOTES\\hyd.info","a") as fp:
    while(True):
        kbddata=input()
        if(kbddata=="@"):
            print("Data written to the file")
            break
        else:
            fp.write(kbddata+"\n")

