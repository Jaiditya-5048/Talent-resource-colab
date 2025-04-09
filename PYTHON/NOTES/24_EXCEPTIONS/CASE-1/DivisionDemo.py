#DivisionDemo.py----Main Program
from Hyd import DivisionByZero
from DivisionOp import divsion
try:
    a=float(input("Enter First Value:"))
    b = float(input("Enter Second Value:"))
    res=divsion(a,b) # Function Call--Gives Either ANS or Exception will come
except DivisionByZero:
    print("\t\tDon't enter zero for den...")
else:
    print("Div({},{})={}".format(a,b,res))

#Phase-3: Handling the exceptions for giving User-Friendly Error Messages.