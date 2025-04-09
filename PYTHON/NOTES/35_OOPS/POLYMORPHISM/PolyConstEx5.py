# PolyConstEx4.py
class Circle:
    def draw(self):  # Method
        print("Drawing Circle")
class Rect:
    def draw(self):  # Method
        print("Drawing Rect")
class Square(Circle,Rect):
    def draw(self): # Overridden Method
        print("Drawing Square")
        Circle.draw(self)
        Rect.draw(self)

# Main Program
s = Square()  # Object Creation--PVM Calls Constructor
s.draw()

