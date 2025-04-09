#Program for Finding Biggest of Two Numbers  by using functions
#FunBigTwoEx1.py
def maxtwo(a,b):
    if(a>b):
        print("max({},{})={}".format(a,b,a))
    elif(b>a):
        print("max({},{})={}".format(a,b,b))
    else:
        print("Both Values are Equal")
#Main Program
print("Enter Two Numerical values")
a,b=float(input()),float(input())
maxtwo(a,b) # Function call
print("Program Execution Completed")
