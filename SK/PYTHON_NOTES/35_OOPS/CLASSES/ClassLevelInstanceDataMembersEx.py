#program for Demonstrating Both Class Level and Instance Data Members
#ClassLevelInstanceDataMembersEx.py
class Student:
    crs = "PYTHON" # here crs is called Class Level Data Members

#Main Program
#Creating Two Objects of Student Class
s1=Student()
s2=Student()
#Place Instance Data Members in s1
s1.sno=int(input("Enter First Student Number:"))
s1.sname=input("Enter First Student Name:")
s1.marks=float(input("Enter First Student Marks:"))
print("----------------------------------")
#Place Instance Data Members in s2
s2.sno=int(input("Enter Second Student Number:"))
s2.sname=input("Enter Second Student Name:")
s2.marks=float(input("Enter Second Student Marks:"))
#Here sno,sname and marks are called Instance Data members
print("First Student Data")
print("\tStudent Number=",s1.sno)
print("\tStudent Name=",s1.sname)
print("\tStudent Marks=",s1.marks)
print("\tSTUDENT COURSE=",Student.crs)
print("----------------------------------")
print("Second Student Data")
print("\tStudent Number=",s2.sno)
print("\tStudent Name=",s2.sname)
print("\tStudent Marks=",s2.marks)
print("\tSTUDENT COURSE=",Student.crs)
print("----------------------------------")



