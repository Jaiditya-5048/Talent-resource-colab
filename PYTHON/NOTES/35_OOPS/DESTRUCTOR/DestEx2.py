#Program for Demonstrating Gabrabe Collector
#DestEx2.py
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
		global memspace
		print("GC calls __del__(self)", id(self))
		memspace=memspace-sys.getsizeof(self)
		print("Now Available Memory With Program=",memspace)
		
#Main Program
print("Program Execution Started")
eo1=Employee(100,"RS")
eo2=Employee(200,"TR")
eo3=Employee(300,"SR")
memspace=sys.getsizeof(eo1)+sys.getsizeof(eo2)+sys.getsizeof(eo3)
print("Total memory Space=",memspace)
print("Program Execution Ended")
time.sleep(5)
#In This Program GC calls Its Destructor at the end of Program execution and This Process is called Automatic Garbage Collection.