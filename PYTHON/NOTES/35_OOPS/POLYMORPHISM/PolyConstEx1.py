#PolyConstEx1.py
class Circle:
    def __init__(self): # Original Constructor
        print("Circle--Default Constructor")

class Rect(Circle):
    def __init__(self): # Overridden Constructor
        print("Rect--Default Constructor")
        super().__init__()

#Main Program
r=Rect() # Object Creation--PVM Calls Constructor