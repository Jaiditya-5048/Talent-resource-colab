#Program for Demonstrating Random Access Files
#RandomAccessFilesEx.py
with open("E:\\KVR-PYTHON-11AM\\FILES\\NOTES\\hyd.info","r") as fp:
    index=fp.tell()
    print("Initially Fp points to:",index)
    filedata=fp.read(3)
    print(filedata) # HYD
    print("Now fp Points tp:",fp.tell())
    print("------------------------------------")
    filedata = fp.read(7)
    print(filedata)  # __is_the
    print("Now fp Points tp:", fp.tell())
    print("------------------------------------")
    filedata = fp.read(8)
    print(filedata)  #
    print("Now fp Points tp:", fp.tell())
    print("------------------------------------")
    filedata = fp.read(30)
    print(filedata)  #
    print("Now fp Points tp:", fp.tell())
    print("------------------------------------")
    filedata = fp.read()
    print(filedata)  #
    print("Now fp Points tp:", fp.tell())
    print("------------------------------------")
    filedata = fp.read()
    print(filedata)  #
    print("Now fp Points tp:", fp.tell())
    print("------------------------------------")
    #resent the fp to specified Index in a file
    fp.seek(11)
    filedata = fp.read(7)
    print(filedata)  #
    print("Now fp Points tp:", fp.tell())
    print("------------------------------------")
    # resent the fp to begining of the  file
    fp.seek(0)
    print("Now fp Points tp:", fp.tell())
    filedata = fp.read(180)
    print(filedata)  #
    print("Now fp Points tp:", fp.tell())
    print("------------------------------------")




