#Program for Performing all Arithmetic Operations by using Multi Line assignment Operator
#AssignmentOpEx1.py
a,b=float(input("Enter First Value:")),float(input("Enter Second Value:")) # Multi Line assignment Operator
sm,sb,ml,ndv,fdv,md,ep=a+b,a-b,a*b,a/b,a//b,a%b,a**b # Multi Line assignment Operator
print("*"*50)
print("\tArithmetic Operations by using Multi LineAssigment Operator")
print("*"*50)
print("\t({}+{})={}".format(a,b,sm))
print("\t({}-{})={}".format(a,b,sb))
print("\t({}*{})={}".format(a,b,ml))
print("\t({}/{})={}".format(a,b,ndv))
print("\t({}//{})={}".format(a,b,fdv))
print("\t({}%{})={}".format(a,b,md))
print("\t({}**{})={}".format(a,b,ep))
print("*"*50)
