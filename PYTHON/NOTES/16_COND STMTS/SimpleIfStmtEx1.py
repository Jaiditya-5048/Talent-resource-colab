#Program for Finding biggest among Two Numerical values
#SimpleIfStmtEx1.py
a=float(input("Enter First Value:")) # a=20
b=float(input("Enter Second Value:"))# b=20
if(a>b):
    print("Max({},{})={}".format(a,b,a))
if(b>a):
    print("Max({},{})={}".format(a,b,b))
if(a==b):
    print("Both Values are equal")
print("Program execution completed")