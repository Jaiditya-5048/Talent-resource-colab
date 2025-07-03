#Program for Demonstrating Default Constructor
#DefaultConstEx1.py
class Test:
	def __init__(self):
		print("I am from Default  Constructor")
		self.a=10
		self.b=20
		print("\tVal of a={}".format(self.a))
		print("\tVal of b={}".format(self.b))

	
#Main Program
t1=Test() # Object Creation calls Default Const
t2=Test() # Object Creation calls Default Const
t3=Test() # Object Creation calls Default Const


	