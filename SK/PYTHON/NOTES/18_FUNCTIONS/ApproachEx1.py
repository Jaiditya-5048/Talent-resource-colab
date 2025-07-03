#Write a Python Program " To Add Two Number " by using functions.
#ApproachEx1.py
#Input   : Taking From Funtion Call
#Process : Done in Function Body
#Result  : Giving Function call
def addop(a,b): # Here 'a' and 'b' are called formal Parameters
    c=a+b # here c is called local variable
    return c
    #return is keyword used for Retruning the Function Processing Logic Result to main program

#Main Program
x=float(input("Enter First Value:"))
y=float(input("Enter Second Value:"))
res=addop(x,y) # function call
print("Sum({},{})={}".format(x,y,res))
print("--------------------------------------------")
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
c=addop(a,b) # function call
print("\t{}+{}={}".format(a,b,c))
print("--------------------------------------------")