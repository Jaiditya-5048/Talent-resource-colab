#Program for Demonstrating globals()
# Here we observed global and local var names are Unique OR Different
#GlobalFunsEx1.py
a=10
b=20
c=30
d=40 # here a,b,c,d are called global Varaibles 
def  operations():
	x=100
	y=200
	z=300
	k=400 # here x,y,z, k are called Local Variables
	res=a+b+c+d+x+y+z+k
	print("sum=",res)

#Main Program
operations() # function call