#Program for Demonstrating the Need of Constructors
#ConstEx1.py
class Emp:
	def __init__(self): # Default Constructor OR Parameter-Less Constructor
		print("I am from Default  Constructor")
		self.eno=100
		self.ename="RS"
		

#Main Program
eo1=Emp() # Object Creation--Makes the PVM to Call Default  Constructor
print("Content of eo=",eo1.__dict__)
eo2=Emp() # Object Creation--Makes the PVM to Call Default  Constructor
print("Content of eo=",eo2.__dict__)
eo3=Emp() # Object Creation--Makes the PVM to Call Default  Constructor
print("Content of eo=",eo3.__dict__)
