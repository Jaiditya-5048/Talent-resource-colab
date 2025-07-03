#Student.py<---File Name and Module Name
from College import College as C
class Student(C):
    def getstuddet(self):
        self.sno=int(input("Enter Student Number:"))
        self.sname=input("Enter Student Name:")
        self.crs=input("Enter Student Course:")
        self.getcolldet()
    def dispstuddet(self):
        self.dispunivdet()
        self.dispcolldet()
        print("-" * 50)
        print("\tStudent Number:{}".format(self.sno))
        print("\tStudent Name:{}".format(self.sname))
        print("\tStudent Course:{}".format(self.crs))
        print("-" * 50)
