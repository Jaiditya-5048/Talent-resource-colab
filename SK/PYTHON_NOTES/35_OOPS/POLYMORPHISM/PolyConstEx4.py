# PolyConstEx4.py
class Circle:
    def __init__(self):  # Original Constructor
        print("Circle--Default Constructor")
class Rect:
    def __init__(self):  # Original Constructor
        print("Rect--Default Constructor")
class Square(Circle,Rect):
    def __init__(self): # Overridden Constructor
        print("Square--Default Constructor")
        super().__init__()
        Rect.__init__(self)

# Main Program
s = Square()  # Object Creation--PVM Calls Constructor