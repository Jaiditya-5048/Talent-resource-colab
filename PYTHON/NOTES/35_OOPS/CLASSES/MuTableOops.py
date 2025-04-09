#MuTableOops.py
class MulTable:
    def read(self):
        self.n=int(input("Enter a Number for Generating MulTable"))
    def table(self):
        if(self.n<=0):
            print("{} is Invalid input".format(self.n))
        else:
            print("-"*50)
            print("Mul Table for :{}".format(self.n))
            print("-" * 50)
            for i in range(1,11):
                print("\t{} x {}={}".format(self.n,i,self.n*i))
            print("-" * 50)
#Main Program
m=MulTable()
m.read()
m.table()