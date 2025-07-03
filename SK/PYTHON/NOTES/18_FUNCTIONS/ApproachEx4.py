#Write a Python Program " To Add Two Number " by using functions.
#ApproachEx4.py
#Input: Inside of Function body
#Process: one in Function Body
#Result: Giving Function call
def addop():
    #Taking Input in Function Body
    a = float(input("Enter First Value:"))
    b = float(input("Enter Second Value:"))
    #Processing
    c=a+b
    #Give the Result back to Function call
    return a,b,c # return stmt can return one or more number of values
#Main Program
a,b,c=addop() # function call with multi line assigment
print("sum({},{})={}".format(a,b,c))
print("-----------------------------------")
r=addop() # Function call with Single Line assigment
#here r is an object of type <class, tuple>
print("sum({},{})={}".format(r[0:1],r[1:2],r[2:3]))
print("-------------OR-----------------------")
print("sum({},{})={}".format(r[-3],r[-2],r[-1]))
