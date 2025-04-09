#MatchCaseStmtEx1.py
print("="*50)
print("\tArithmetic Operations")
print("="*50)
print("\t1.Addition")
print("\t2.Substraction")
print("\t3.Multiplication")
print("\t4.Division")
print("\t5.Modulo Division")
print("\t6.Exponentiation")
print("\t7.Exit")
print("="*50)
ch=int(input("Enter UR Choice:"))
match(ch):

    case 1:
        print("Enter Two Values for Addition:")
        a,b=float(input()),float(input())
        print("\tSum({},{})={}".format(a,b,a+b))
    case 2:
        print("Enter Two Values for Substraction:")
        a, b = float(input()), float(input())
        print("\tSub({},{})={}".format(a, b, a - b))
    case 3:
        print("Enter Two Values for Multiplication:")
        a, b = float(input()), float(input())
        print("\tMul({},{})={}".format(a, b, a * b))
    case 4:
        print("Enter Two Values for Division:")
        a, b = float(input()), float(input())
        print("\tDiv({},{})={}".format(a, b, a / b))
        print("\tFloor Div({},{})={}".format(a, b, a // b))
    case 6:
        a, b = float(input("Enter Base:")), float(input("Enter Power:"))
        print("pow({},{})={}".format(a,b,a**b))
    case 5:
        print("Enter Two Values for Division:")
        a, b = float(input()), float(input())
        print("\tModDiv({},{})={}".format(a, b, a % b))
    case 7:
        print("Thx for using Program")
    case _:
        print("Ur Selection of Operation is Wrong--try again")
print("Program execution Completed")