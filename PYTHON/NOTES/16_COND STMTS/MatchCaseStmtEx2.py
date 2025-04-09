#MatchCaseStmtEx2.py
s="""********************************************************************
	Area of Different Figures
	*********************************************************************
		R. Rectangle
		S. Square
		C. Circle
		T. Triangle
		E. Exit
	*********************************************************************
		Enter Ur Choice:
	*********************************************************************"""
print(s)
ch=input("Enter Ur Choice:")
match(ch.upper()):
    case "R":
        print("Enter Length and Breadth:")
        L,B=float(input()),float(input())
        print("Area of Rect={}".format(L*B))
    case "S":
        s=float(input("Enter Side:"))
        print("Area of Square={}".format(s**2))
    case "C":
        r=float(input("Enter Radius:"))
        print("Area of Circle={}".format(3.14*r**2))
    case "T":
        B,H=float(input("Enter Base:")),float(input("Enter Height:"))
        print("Area of Triangle={}".format((1/2)*B*H))
    case "E":
        print("Thx for Using Program")
    case _:
        print("Ur Selection of Operation wrong--try again")