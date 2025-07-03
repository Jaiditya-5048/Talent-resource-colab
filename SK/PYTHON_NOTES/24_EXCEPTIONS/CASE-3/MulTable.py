#MulTable.py<----File Name and Module Name
from MulTabExceptions import NegativeNumError,ZeroError
def table(n):
    if(n<0):
        raise NegativeNumError
    elif(n==0):
        raise ZeroError
    else:
        print("*"*50)
        print("Mul Table for:{}".format(n))
        print("*" * 50)
        for i in range(1,11):
            print("\t{}x{}={}".format(n,i,n*i))
        print("*" * 50)