#InhProg4.py
class Univ:
    def getunivdet(self):
        self.uname=input("Enter University Name:")
        self.uloc = input("Enter University Location:")
    def dispunivdet(self):
        print("-"*50)
        print("\tUniverisy Name:{}".format(self.uname))
        print("\tUniverisy Location:{}".format(self.uloc))
        print("-" * 50)
class College(Univ):
    def getcolldet(self):
        self.cname=input("Enter College Name:")
        self.cloc = input("Enter College Location:")
    def dispcolldet(self):
        print("-"*50)
        print("\tCollege Name:{}".format(self.cname))
        print("\tCollege Location:{}".format(self.cloc))
        print("-" * 50)
class Student(College):
    def getstuddet(self):
        self.sno=int(input("Enter Student Number:"))
        self.sname=input("Enter Student Name:")
        self.crs=input("Enter Student Course:")
    def dispstuddet(self):
        print("-" * 50)
        print("\tStudent Number:{}".format(self.sno))
        print("\tStudent Name:{}".format(self.sname))
        print("\tStudent Course:{}".format(self.crs))
        print("-" * 50)
#Main Program
s=Student()
s.getstuddet()
s.getcolldet()
s.getunivdet()
s.dispunivdet()
s.dispcolldet()
s.dispstuddet()
