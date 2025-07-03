#ATMOperations.py<----File Name and Module Name
from ATMExcept import DepositError,WithdrawError,InSuffFundError
bal=500.00 # Global Variable
def deposit():
    damt=float(input("Enter Ur Deposit Amount:")) # implcitly raising ValueError in the case non-num vals
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Ur Account xxxxxxxxx123 Credited with INR:{}".format(damt))
        print("Now Ur Account xxxxxxxxx123 Bal after Deposit INR:{}".format(bal))
def withdraw():
    global bal
    wamt = float(input("Enter Ur Withdraw Amount:")) # implcitly raising ValueError in the case non-num vals
    if(wamt<=0):
        raise WithdrawError
    elif((wamt+500)>bal):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("Ur Account xxxxxxxxx123 Debited with INR:{}".format(wamt))
        print("Now Ur Account xxxxxxxxx123 Bal after withdraw INR:{}".format(bal))

def balenq():
    print("Now Ur Account xxxxxxxxx123 Bal INR:{}".format(bal))