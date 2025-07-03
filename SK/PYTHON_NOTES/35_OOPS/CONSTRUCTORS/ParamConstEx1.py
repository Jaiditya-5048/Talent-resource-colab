#Program for Demonstrating Parameterized Constructor
#ParamConstEx1.py
class Test:
	def __init__(self,a,b):
		print("I am from Parameterized  Constructor")
		self.a=a
		self.b=b
		print("\tVal of a={}".format(self.a))
		print("\tVal of b={}".format(self.b))

	
#Main Program
t1=Test(10,20) # Object Creation calls Parameterized Const
t2=Test(100,200) # Object Creation calls Parameterized Const
t3=Test(1000,2000) # Object Creation callsParameterized Const