#CircleArea.py
class Circle:
    @classmethod
    def getPI(cls):
        cls.PI=3.14
    def getrad(self):
        self.r=float(input("Enter Radius:"))
    def calarea(self):
        Circle.getPI()
        self.ac=Circle.PI*self.r**2
    def disparea(self):
        print("Radius={}".format(self.r))
        print("Area of Circle={}".format(self.ac))

#main Program
c=Circle()
c.getrad()
c.calarea()
c.disparea()