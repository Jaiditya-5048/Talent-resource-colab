#This Program Demonstrates How to place Class Level Data Members
#ClassLevelDataMembersEx1.py
class Student:
    crs="PYTHON"
    cnt="INDIA"  # Here crs and cnt are called Class Level Data Members

#Main Program
print("Student Course Name=",Student.crs)
print("Student Country=",Student.cnt)