#InhProg3.py
class A:
    def getA(self):
        self.x=100
class B:
    def getB(self):
        self.y=200
class C(A,B):
    def operation(self):
        self.getA()
        self.getB()
        self.c=self.x+self.y
        print("sum({},{})={}".format(self.x,self.y,self.c))

#Main Program
co=C()
co.operation()



