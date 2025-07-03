#InstanceMethodEx1.py
class Student:
    def readstuddata(self,objinfo):
        print("-" * 50)
        print("Enter {} Object Information".format(objinfo))
        print("-"*50)
        self.sno=int(input("Enter Student Number:"))
        self.sname=input("Enter Student Name:")
        self.marks=float(input("Enter Student Marks"))
        print("-" * 50)
    def dispstuddata(self,objinfo):
        print("-" * 50)
        print("{} Object Information".format(objinfo))
        print("-" * 50)
        print("\tStudent Number=", self.sno)
        print("\tStudent Name=", self.sname)
        print("\tStudent Marks=", self.marks)
        print("-" * 50)
#Main Program
s1=Student()
s1.readstuddata("First")
s2=Student()
s2.readstuddata("Second")
#Display Student Object data.
s1.dispstuddata("First")
s2.dispstuddata("Second")
