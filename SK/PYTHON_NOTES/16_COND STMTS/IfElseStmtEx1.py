#Program for accepting Two Values anf find Biggest among them
#IfElseStmtEx1.py
a=float(input("Enter First Value:")) # 200
b=float(input("Enter Second Value:")) # 100
if(a>b):
    print("big({},{})={}".format(a,b,a))
else:
    print("big({},{})={}".format(a,b,b))
print("Program Execution Completed")