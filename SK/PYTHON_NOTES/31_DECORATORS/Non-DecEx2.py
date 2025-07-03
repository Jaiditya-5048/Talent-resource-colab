#Program for demononstrating Non-Decorators
#Non-DecEx2.py
def  getval(op):  # This is the Function Defined by KVR
	return float(input("Enter a Value for Calculating {}:".format(op)))

def sqaure():						#Pavan is asking sir give square 5
	n=getval("Square")
	res=n**2
	print("sqaure({})={}".format(n,res))

def squareroot():						#Raju is asking sir  give squre root 5
	n=getval("Square Root")
	res=n**0.5
	print("SquareRoot({})={}".format(n,res))

def cuberoot():						#Teja is asking give cube root of 5
	n=getval("Cube Root")
	res=n**(1/3)
	print("cuberoot({})={}".format(n,res))

#Main Program
sqaure()
squareroot()
cuberoot()