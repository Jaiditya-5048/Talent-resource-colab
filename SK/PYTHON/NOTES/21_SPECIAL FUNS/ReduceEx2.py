#Program for Finding Sum of List of Values by using reduce()
#ReduceEx2.py
import functools
def sumop(a,b):
	return (a+b)

#Main Program
print("Enter list of Values separated by space:")
lst=[float(val) for val in input().split()]
res=functools.reduce(sumop, lst)
print("sum=",res)