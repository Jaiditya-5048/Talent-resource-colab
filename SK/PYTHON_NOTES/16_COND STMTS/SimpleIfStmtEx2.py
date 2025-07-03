#Program for Finding biggest among Three Numerical values
#SimpleIfStmtEx2.py
a=float(input("Enter First Value:")) # 10
b=float(input("Enter Second Value:")) # 10
c=float(input("Enter Third Value:")) # 10
if(a>=b) and (a>c):
    print("Max({},{},{})={}".format(a,b,c,a))
if(b>a) and (b>=c):
    print("Max({},{},{})={}".format(a,b,c,b))
if(c>=a) and (c>b):
    print("Max({},{},{})={}".format(a,b,c,c))
if(a==b) and (b==c) and (c==a):
    print("Max({},{},{})={}".format(a,b,c,"All values are equal"))
print("Program Execution Over")

