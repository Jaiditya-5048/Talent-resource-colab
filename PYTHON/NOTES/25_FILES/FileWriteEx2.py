#Program for Demnstrating How to write the Data to the file
#FileWriteEx2.py
sno=int(input("Enter Student Number:"))
sname=input("Enter Student Name:")
marks=float(input("Enter Student Marks:"))
#write OR save the above student data in file
with open("stud.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
    print("Data Written to the File")

