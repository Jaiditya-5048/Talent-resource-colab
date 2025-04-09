#This Program Demonstrates How to Palce Instance Data Members
#InstanceDataMembersEx2.py
class Student:pass

#Main Program
#Creating Two Objects of Student Class
s1=Student()
s2=Student()
print("Memory Address of s1=",id(s1))
print("Memory Address of s2=",id(s2))
print("----------------------------------")
#Place Instance Data Members in s1
s1.sno=100
s1.sname='Rossum'
s1.marks=4.5
#Place Instance Data Members in s2
s2.sno=200
s2.sname="Travis"
s2.marks=5.6
#Here sno,sname and marks are called Instance Data members
print("First Student Data")
print("Student Number=",s1.sno)
print("Student Name=",s1.sname)
print("Student Marks=",s1.marks)
print("----------------------------------")
print("Second Student Data")
print("Student Number=",s2.sno)
print("Student Name=",s2.sname)
print("Student Marks=",s2.marks)




