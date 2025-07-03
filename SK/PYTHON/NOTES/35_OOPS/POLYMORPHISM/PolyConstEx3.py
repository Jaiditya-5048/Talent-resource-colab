#PolyConstEx3.py
class Circle:
    def __init__(self): # Original Constructor
        print("Circle--Default Constructor")
class Rect(Circle):
    def __init__(self): # Overridden Constructor
        print("Rect--Default Constructor")
class Square(Rect):
    def __init__(self): # Overridden Constructor
        print("Square--Default Constructor")
        Circle.__init__(self)
        Rect.__init__(self)

#Main Program
s=Square() # Object Creation--PVM Calls Constructor