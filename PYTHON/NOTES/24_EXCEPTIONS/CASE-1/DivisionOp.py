#DivisionOp.py<-----File Name and Module Name
from Hyd import DivisionByZero
def  divsion(a,b):
    if(b==0):
        raise DivisionByZero
    else:
        return (a/b)


#Phase-2:  Defining Common Function with Business Logic
          # and Hitting OR Generating Exception by using raise keyword