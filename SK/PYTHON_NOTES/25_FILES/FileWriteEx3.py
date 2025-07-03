#Program for Demnstrating How to write the Data to the file
#FileWriteEx3.py
x={10:"Python",20:"C",30:"C++"}
with open("stud1.data","a") as fp:
    fp.writelines(str(x)+"\n")
    print("Data Written to the File")

