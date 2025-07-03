#Program for Finding Sum of List of Values by using reduce()
#ReduceEx1.py
import functools
print("Enter list of Values separated by space:")
lst=[float(val) for val in input().split()]
res=functools.reduce(lambda k,v: k+v, lst)
print("sum=",res)