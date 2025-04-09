#Program for Demonstrating Gabrabe Collector
#DestEx5.py
import time
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
		print("GC calls __del__(self)")

#Main Program
print("Program Execution Started")
eo1=Employee(100,"RS")
eo2=eo1 # Deep Copy
eo3=eo1 # Copy Copy
print("No Longer Interested to maintain the memory space of eo1")
time.sleep(5)
eo1=None # Here GC  will not call Destructor Forcelly, bcoz still eo2 and eo3 points to memory space
time.sleep(5)
print("No Longer Interested to maintain the memory space of eo2")
time.sleep(5)
eo2=None # # Here GC  will not call Destructor Forcelly, bcoz still eo1 points to memory space
print("No Longer Interested to maintain the memory space of eo3")
time.sleep(5)
eo3=None #  # Here GC calles Destructor Forcelly
print("Program Execution Ended")
time.sleep(5)

