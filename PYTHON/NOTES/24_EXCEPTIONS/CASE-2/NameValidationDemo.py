#NameValidationDemo.py<---Main Program
from NameValidation import validate
from NameExcept import InvalidNameError,ZeroSizeError
while(True):
    name=input("Enter Ur Name:")
    try:
        res=validate(name) # Function call
    except InvalidNameError:
        print("\t{} is Invalid Name-try again".format(name))
    except ZeroSizeError:
        print("\tDon't Enter Space as Name-try Again")
    else:
        print(res)
        break

