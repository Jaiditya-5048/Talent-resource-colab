#AccessingAccountDet.py
class Account:
    def __init__(self):
        self.__acno=10
        self.cname="RS"
        self.__bal=5.6
        self.__pin=5678
        self.bname="SBI"
    def showaccdeatils(self):
        print("Account Number={}".format(self.__acno))
        print("Account Holder Name={}".format(self.cname))
        print("Account Bal={}".format(self.__bal))
        print("Account Pin={}".format(self.__pin))
        print("Account Branch Name={}".format(self.bname))

#Main Program
ac=Account()
ac.showaccdeatils()