#Program for Demonstrating the NEED of Variable Length Args
#This Program will  execute as it is 
#VarArgsEx2.py
def dispvals(a,b,c,d,e): # Function Def-1
	print(a,b,c,d,e)

dispvals(10,20,30,40,50) # Function call-1 with Pos Args-----5
#-------------------------------------------------------------------
def dispvals(a,b,c,d): # Function Def-2
	print(a,b,c,d)

dispvals(10,20,30,40)   # Function call-2 with Pos Args-----4
#-----------------------------------------------------------------
def dispvals(a,b,c): # Function Def-3
	print(a,b,c)

dispvals(10,20,30)   # Function call-3 with Pos Args-----3
#-----------------------------------------------------------------
def dispvals(a,b): # Function Def-4
	print(a,b)
dispvals(10,20)   # Function call-4 with Pos Args-----2
#-----------------------------------------------------------------
def dispvals(a): # Function Def-5
	print(a)
dispvals(10)   # Function call-5 with Pos Args-----1
#-----------------------------------------------------------------
def dispvals(): # Function Def-6
	print("empty")
dispvals()   # Function call-6 with Pos Args-----0
#-----------------------------------------------------------------

#NOTE: Accorinf to the above Program
# If we have n-Number of Family Simlar Function calls then we Must Define N-Number of Function definitions 
# This Procees if Time Consuming and Lots of Development time is waste
# We are looking For ONE FUNCTION DEFINITION for n-Number of Family Simlar Function calls--dine by Variable Length Args