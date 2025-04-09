#Program for accepting Numerical and Decide whether It is +Ve or -Ve or zero
#IfElseStmtEx3.py
n=float(input("Enter a Number:"))
if(n>0):
    print("{} is +VE".format(n))
else:
    if(n==0):
        print("{} is ZERO".format(n))
    else:
        print("{} is -VE".format(n))
