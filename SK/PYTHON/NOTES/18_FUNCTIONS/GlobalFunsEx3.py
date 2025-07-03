#Program for Demonstrating globals()
# Here we observed global and local var names are SAME
#GlobalFunsEx3.py
a=10
b=20
c=30
d=40 # here a,b,c,d are called global Varaibles 
def  operations():
	a=100
	b=200
	c=300
	d=400 # here a,b,c,d are called Local Variables
	res=a+b+c+d+globals()['a']+globals()['b']+globals().get('c')+globals().get('d')
	print("sum=",res)

#Main Program	
operations() # function call   