#Program for demononstrating Decorators
#DecEx2.py
def square(gv): # Decorator Function
	def processval():
		n=gv()
		res=n**2
		return n,res
	return processval

@square
def  getval():  # This is the Function Defined by KVR
	return float(input("Enter a Number:"))


#Main Program
num,result=getval() # Normal Function Call
print("square({})={}".format(num,result))