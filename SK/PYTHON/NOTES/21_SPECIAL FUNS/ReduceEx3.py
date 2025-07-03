#Program for Finding Maximum Element from List of Values by using reduce()
#ReduceEx3.py
import functools

#Main Program
print("Enter list of Values separated by space:") 
lst=[float(val) for val in input().split()]
maxv=functools.reduce(lambda k,v: k if k>v else v, lst)
print("Biggest Value=",maxv)

