#Program for Demonstrating global Key word
#GlobalKwdEx1.py
def  incr():
	global a
	a=a+1

#Main Program
a=10 # Here 'a' is called Global Variable
print("Main Prog: Val of a before incr() call={}".format(a)) # 10
incr() # Function Call
print("Main Prog: Val of a after incr() call={}".format(a))