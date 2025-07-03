#Program for Demonstrating Gabrabe Collector
#DestEx4.py
import sys,time
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
print("No Longer Interested to maintain the memory space of eo1")
time.sleep(5)
eo1=None # Here GC calles Destructor Forcelly
time.sleep(5)
eo2=Employee(200,"TR")
print("No Longer Interested to maintain the memory space of eo2")
time.sleep(5)
eo2=None # Here GC calles Destructor Forcelly
eo3=Employee(300,"SR")
print("No Longer Interested to maintain the memory space of eo3")
time.sleep(5)
eo3=None
print("Program Execution Ended")
time.sleep(5)