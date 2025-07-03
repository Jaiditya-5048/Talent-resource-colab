#Program for Demonstrating the need of Static Method
#StaticMethodEx1.py
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

class HYD:
	@staticmethod
	def  dispobjectdata(objdata,objinfo ):
		print("-"*50)
		print("{} Object Information".format(objinfo))
		print("-"*50)
		for dmn,dmv in objdata.__dict__.items():
			print("\t{}--->{}".format(dmn,dmv))
		print("-"*50)
		
#Main Program
s=Student()
e=Employee()
t=Teacher()
print("-----------------------------------------------------------")
#Place the Instance Data in Student Object--s
s.readstuddata()
print("-----------------------------------------------------------")
#Place the Instance Data in Employee Object--e
e.readempdata()
print("-----------------------------------------------------------")
#Place the Instance Data in Teacher Object--t
t.readteacherdata()
#We are taking One Method for displaying all the Objects of any Class and such is method is called Static Method
HYD.dispobjectdata(s,"Student") # Here s is an object of student class
HYD.dispobjectdata(e,"Employee") # Here e is an object of Employee class
HYD.dispobjectdata(t,"Teacher") # Here t is an object of Teacher class

				