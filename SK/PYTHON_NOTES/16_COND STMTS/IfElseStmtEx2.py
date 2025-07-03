#Program for accepting Two Values anf find Biggest among them
#IfElseStmtEx2.py
a=float(input("Enter First Value:")) # 10
b=float(input("Enter Second Value:")) # 10
if(a>b):
    print("big({},{})={}".format(a,b,a))
else:
    if(b>a):
        print("big({},{})={}".format(a,b,b))
    else:
        print("Both Values are equal")
    print("Other Stmts--for inner if ..else")
print("Other Stmts--for outer if ..else")
print("Program Execution Over")