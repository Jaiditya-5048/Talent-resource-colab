#Program for Demonstrating globals()
#GlobalFunsEx2.py
a=10
b=20 # here a,b are called global Varaibles 
def  operations():
	d=globals()
	print("-"*50)
	print("List Visible and Invisible Global Variables")
	print("-"*50)
	for gvn,gvv in d.items():
			print("{}---->{}".format(gvn,gvv))
	print("-"*50)
	print("Programmer-Defined Global Variables--way-1")
	print("Global Var a={}".format(d.get('a')))
	print("Global Var b={}".format(d.get('b')))
	print("-"*50)
	print("Programmer-Defined Global Variables--way-2")
	print("Global Var a={}".format(d['a']))
	print("Global Var b={}".format(d['b']))
	print("-"*50)
	print("Programmer-Defined Global Variables--way-3")
	print("Global Var a={}".format(globals()['a']))
	print("Global Var b={}".format(globals()['b']))
	print("-"*50)
	print("Programmer-Defined Global Variables--way-4")
	print("Global Var a={}".format(globals().get('a')))
	print("Global Var b={}".format(globals().get('b')))
	print("-"*50)
#Main Program	
operations() # function call   