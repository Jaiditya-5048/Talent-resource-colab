#Program for Demonstrating Gabrabe Collector
#DestEx5.py
class Employee:
	def __init__(self,eno,ename):
		print("--------------------------------------------")
		print("I am from Constructor")
		self.eno=eno
		self.ename=ename
		print("Emp No=",self.eno)
		print("Emp Name=",self.ename)
		print("--------------------------------------------")
	def  __del__(self):
		print("GC calls __del__(self)", id(self))

#Main Program
print("Program Execution Started")
eo1=Employee(100,"RS")
eo2=eo1 # Deep Copy
eo3=eo1 # Copy Copy
print("Program Execution Ended")
