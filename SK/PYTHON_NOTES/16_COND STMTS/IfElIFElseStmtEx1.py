#Program for accepting Two Values anf find Biggest among them
#IfElIFElseStmtEx1.py
a=float(input("Enter First Value:")) # 10
b=float(input("Enter Second Value:")) # 2
if(a==b):
    print("Both Values are Equal")
elif(a>b):
    print("max({},{})={}".format(a,b,a))
else:
    print("max({},{})={}".format(a, b, b))
print("Program Execution completed")