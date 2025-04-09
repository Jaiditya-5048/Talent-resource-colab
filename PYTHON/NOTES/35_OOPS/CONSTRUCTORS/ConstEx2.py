#Program for Demonstrating the Need of Constructors
#ConstEx2.py
class Emp:
	def __init__(self,empno,ename): # Parameterized Constructor
		print("I am from Parameterized Constructor")
		self.eno=empno
		self.ename=ename
		
#Main Program
eo1=Emp(10,"Rossum") # Object Creation--Makes the PVM to Call Parameterized Constructor
print("Content of eo=",eo1.__dict__)
eo2=Emp(20,"Travis") # Object Creation--Makes the PVM to Call Parameterized Constructor
print("Content of eo=",eo2.__dict__)
eo3=Emp(30,"Jhunter") # Object Creation--Makes the PVM to Call Parameterized Constructor
print("Content of eo=",eo3.__dict__)
