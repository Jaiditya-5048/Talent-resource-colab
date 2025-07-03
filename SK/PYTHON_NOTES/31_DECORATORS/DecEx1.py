#Program for demononstrating Decorators
#DecEx1.py
def  getval():  # This is the Function Defined by KVR
	return float(input("Enter a Number:"))

def  square(hyd): # Decorator Definition
	def  caculate(): # Inner Function Def..
		n=hyd()
		res=n**2
		return n,res
	return caculate

#Main Program
calc=square(getval) # Decorator Call--Here square is a decorator bcoz It takes Normal Function as argument
num,result=calc()
print("Square({})={}".format(num,result))
