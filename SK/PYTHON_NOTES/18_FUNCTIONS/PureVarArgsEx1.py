#Program for Demonstrating the The Functionality of Variable Length Args
#PureVarArgsEx1.py
def  dispvals( *kvr): # Here *kvr is called Variable length Parameter and whose type is <class,tuple>
	print(kvr,type(kvr),len(kvr))



#Main Program
dispvals(10,20,30,40,50) # Function call-1 with Pos Args-----5
dispvals(10,20,30,40)   # Function call-2 with Pos Args-----4
dispvals(10,20,30)   # Function call-3 with Pos Args-----3
dispvals(10,20)   # Function call-4 with Pos Args-----2
dispvals(10)   # Function call-5 with Pos Args-----1
dispvals()   # Function call-6 with Pos Args-----0