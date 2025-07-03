#College.py<----File Name and Module Name
from Univ import Univ
class College(Univ):
    def getcolldet(self):
        self.cname=input("Enter College Name:")
        self.cloc = input("Enter College Location:")
        self.getunivdet()
    def dispcolldet(self):
        print("-"*50)
        print("\tCollege Name:{}".format(self.cname))
        print("\tCollege Location:{}".format(self.cloc))
        print("-" * 50)
