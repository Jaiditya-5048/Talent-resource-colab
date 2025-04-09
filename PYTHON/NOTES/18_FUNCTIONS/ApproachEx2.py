#Write a Python Program " To Add Two Number " by using functions.
#ApproachEx2.py
#Input : Taking Inside of Function body
#PROCESS: Done in Function Body
#Output: Displayed in function body
def addop():
    #Taking INPUT inside of Function Body
    a=float(input("Enter First Value:"))
    b = float(input("Enter Second Value:"))
    #Process inside of Function Body
    c=a+b
    #Display the Result in Function Body
    print("sum({},{})={}".format(a,b,c))
#Main Program
print("I am before Function call")
addop()  # Function Call
print("------------------------------")
print("I am after Function call")
