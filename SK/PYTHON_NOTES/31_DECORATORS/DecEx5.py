#Program for demononstrating Decorator to Decorator
#DecEx5.py
def cuberoot(cv):
	def calcbrt():
		n,sqv,sqrtv=cv()
		cbrtv=n**(1/3)
		return n,sqv,sqrtv,cbrtv
	return calcbrt

def squareroot(kvr):
	def  calsqrt():
		n,sqres=kvr()
		sqrtres=n**0.5
		return n,sqres,sqrtres
	return calsqrt

def square(gv): # Decorator Function
	def processval():
		n=gv()
		res=n**2
		return n,res
	return processval

@cuberoot
@squareroot
@square
def  getval():  # This is the Function Defined by KVR
	return float(input("Enter a Number:"))


#Main Program
num,sqresult,sqrtresult,cbrtresult=getval() # Normal Function Call
print("square({})={}".format(num,sqresult))
print("squareroot({})={}".format(num,sqrtresult))
print("cuberoot({})={}".format(num,cbrtresult))