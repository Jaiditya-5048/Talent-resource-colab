#Write a Python Program " To Add Two Number " by using functions.
#ApproachEx3.py
#Input:  Taking From Funtion Call
#Process: Done in Function Body
#Result:  Displayed in function body
def addop(a,b):
    c=a+b
    print("Sum({},{})={}".format(a,b,c))

#main Program
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
addop(a,b) # Function call