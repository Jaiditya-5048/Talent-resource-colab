#Program for Demonstrating the need of Static Method
#MultipleClassesObjects.py
class Student:
	def readstuddata(self):
		self.sno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")

class Employee:
	def readempdata(self):
		self.eno=int(input("Enter Employee Number:"))
		self.ename=input("Enter Employee Name:")
		self.sal=float(input("Enter Employee Salary:"))

class Teacher:
	def readteacherdata(self):
		self.tno=int(input("Enter Teacher Number:"))
		self.tname=input("Enter Teacher Name:")
		self.subject=input("Enter Teacher Subject:")
		self.expe=float(input("Enter Teacher Exp:"))

#Main Program
s=Student()
e=Employee()
t=Teacher()
print("content of s before Reading=",s.__dict__)
print("content of e before Reading=",e.__dict__)
print("content of t before Reading=",t.__dict__)
print("-----------------------------------------------------------")
#Place the Instance Data in Student Object--s
s.readstuddata()
print("-----------------------------------------------------------")
#Place the Instance Data in Employee Object--e
e.readempdata()
print("-----------------------------------------------------------")
#Place the Instance Data in Teacher Object--t
t.readteacherdata()
print("-----------------------------------------------------------")
print("content of s after Reading=",s.__dict__)
print("content of e after Reading=",e.__dict__)
print("content of t after Reading=",t.__dict__)
print("-----------------------------------------------------------")
				