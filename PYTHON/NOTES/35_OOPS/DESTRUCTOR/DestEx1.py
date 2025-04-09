#Program for Demonstrating Gabrabe Collector
#DestEx1.py
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
eo2=Employee(200,"TR")
eo3=Employee(300,"SR")
print("Program Execution Ended")
