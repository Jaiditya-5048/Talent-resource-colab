#Program for demononstrating Non-Decorators
#Non-DecEx1.py
def  getval():  # This is the Function Defined by KVR
	return 5

def sqaure():						#Pavan is asking sir give square 5
	n=getval()
	res=n**2
	print("sqaure({})={}".format(n,res))

def squareroot():						#Raju is asking sir  give squre root 5
	n=getval()
	res=n**0.5
	print("SquareRoot({})={}".format(n,res))

def cuberoot():						#Teja is asking give cube root of 5
	n=getval()
	res=n**(1/3)
	print("cuberoot({})={}".format(n,res))

#Main Program
sqaure()
#squareroot()
#cuberoot()