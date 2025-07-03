#Program for Demnstrating How to write the Data to the file
#FileWriteEx1.py
sno=20
sname="Travis"
marks=55.55
#write OR save the above student data in file
with open("stud.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
    print("Data Written to the File")

