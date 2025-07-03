#PolyEx.py
class Univ:
    def getdet(self):
        self.uname=input("Enter University Name:")
        self.uloc = input("Enter University Location:")
    def dispdet(self):
        print("-"*50)
        print("\tUniverisy Name:{}".format(self.uname))
        print("\tUniverisy Location:{}".format(self.uloc))
        print("-" * 50)
class College(Univ):
    def getdet(self):
        self.cname=input("Enter College Name:")
        self.cloc = input("Enter College Location:")

    def dispdet(self):
        print("-"*50)
        print("\tCollege Name:{}".format(self.cname))
        print("\tCollege Location:{}".format(self.cloc))
        print("-" * 50)
class Student(College):
    def getdet(self):
        self.sno=int(input("Enter Student Number:"))
        self.sname=input("Enter Student Name:")
        self.crs=input("Enter Student Course:")
        College.getdet(self)
        Univ.getdet(self)
    def dispdet(self):
        Univ.dispdet(self)
        College.dispdet(self)
        print("-" * 50)
        print("\tStudent Number:{}".format(self.sno))
        print("\tStudent Name:{}".format(self.sname))
        print("\tStudent Course:{}".format(self.crs))
        print("-" * 50)
#Main Program
s=Student()
s.getdet()
s.dispdet()