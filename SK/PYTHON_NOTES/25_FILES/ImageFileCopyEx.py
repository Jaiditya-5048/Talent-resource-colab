#Program for Copying an Image (Binary file) into another file
#ImageFileCopyEx.py
try:
    with open("E:\\KVR-DSA\\K-V-rao.png","rb") as rp:
        with open("python-faculty.png","wb") as wp:
            #read the data from source file
            srcfiledata=rp.read()
            #write the source file data to the Destination file data
            wp.write(srcfiledata)
            print("Source File Image Data Copied into Destination File")
except FileNotFoundError:
    print("Source File Does not Exist")