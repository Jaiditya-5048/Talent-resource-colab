#Program for Demonstrating Parameterized Constructor and Default Constructor in Same Program
#DefaultParamConstEx1.py
class Test:
	def __init__(self,a=1,b=2):
		print("I am from Default / Parameterized  Constructor")
		self.a=a
		self.b=b
		print("\tVal of a={}".format(self.a))
		print("\tVal of b={}".format(self.b))
	
#Main Program
t1=Test() # Object Creation calls Default Const
t2=Test(100,200) # Object Creation calls Parameterized Const
t3=Test(b=200) # Object Creation calls Parameterized Const
t4=Test(b=400,a=200)# Object Creation calls Parameterized Const


