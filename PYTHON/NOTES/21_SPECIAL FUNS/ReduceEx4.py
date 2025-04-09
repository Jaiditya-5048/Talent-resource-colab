#Program for Finding Maximum Element from List of Values by using reduce()
#ReduceEx4.py
import functools
def findbig(a,b):
	return (a if a>b else b)

#Main Program
print("Enter list of Values separated by space:") 
lst=[float(val) for val in input().split()]
maxv=functools.reduce(findbig, lst)
print("Biggest Value=",maxv)
