#Program for Demonstrating the Need of Constructors
#Non-ConstEx1.py
class Emp:
	def getempdata(self):
		self.eno=10
		self.ename="RS"

#Main Program
eo=Emp() # Object Creation
print("content of eo=",eo.__dict__) # { }
#Call the Instance Method Explcitly by using Object
eo.getempdata() # Method call
print("content of eo=",eo.__dict__) # { }
