#Program for Copying the content of one file into another file
#FileCopyEx.py
try:
    srcfile=input("Enter Source File:")
    with open(srcfile,"r") as rp:
        dstfile=input("Enter Destination File:")
        with open(dstfile,"a") as wp:
            #read the data from source file
            srcfiledata=rp.read()
            #write the source file data to the Destination file data
            wp.write(srcfiledata+"\n")
            print("Source File Data Copied into Destination File")
except FileNotFoundError:
    print("Source File Does not Exist")