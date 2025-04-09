#This Program Demonstrates How to Palce Instance Data Members
#InstanceDataMembersEx1.py
class Student:pass

#Main Program
s=Student()
print("Memory Address of s1=",id(s))
#Place Instance Data Members in s
s.sno=100
s.sname='Rossum'
s.marks=4.5
#Here sno,sname and sal are called Instance Data members
print("Student Number=",s.sno)
print("Student Name=",s.sname)
print("Student Marks=",s.marks)




