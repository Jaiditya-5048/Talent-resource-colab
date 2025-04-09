#MulTableDemo.py<----Main Program
from MulTabExceptions import NegativeNumError,ZeroError
from MulTable import table
try:
    n=int(input("Enter a Number for generating mul table:"))
    try:
        table(n) # Function Call
    except NegativeNumError:
        print("\tDon't Enter -VE Number for Mul Table")
    except ZeroError:
        print("\tDon't Enter Zero for Mul Table")
    except:
        print("Ooops Some thing went wrong!!!")
except ValueError:
    print("Don't Enter alnums,strs and symbols for mul table")