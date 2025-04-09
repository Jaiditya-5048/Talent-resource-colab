#Program for Demonstrating the The Functionality of Variable Length Args
#PureVarArgsEx3.py
def  dispvals(no,pname,dsg, *kvr): # Here *kvr is called Variable length Parameter and whose type is <class,tuple>
	print("-"*50)
	print("Person Number={}".format(no))
	print("Person name:{}".format(pname))
	print("Person Dsg={}".format(dsg))
	print("Number of Values=",len(kvr))
	for val in kvr:
		print("\t{}".format(val))
	print("-"*50)


#Main Program
dispvals(100,"RS","X",10,20,30,40,50) # Function call-1 with Pos Args-----5
dispvals(200,"TR","XII",10,20,30,40)   # Function call-2 with Pos Args-----4
dispvals(300,"MC","B.Tech",10,20,30)   # Function call-3 with Pos Args-----3
dispvals(400,"KN","Pharmacy",10,20)   # Function call-4 with Pos Args-----2
dispvals(500,"JG","Sci",10)   # Function call-5 with Pos Args-----1
dispvals(600,"JH","PM")   # Function call-6 with Pos Args-----0
