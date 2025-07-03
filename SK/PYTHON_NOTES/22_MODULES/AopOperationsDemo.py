#AopOperationsDemo.py-----Program (Not Module )
from Aopmenu import menu
from AopOperations import addop,subop,mulop,divop,modop,expop
while(True):
    menu()
    ch=input("Enter UR Choice:")
    if(ch.isdigit()):
        match(int(ch)):
            case 1:
                addop()
            case 2:
                subop()
            case 3:
                mulop()
            case 4:
                divop()
            case 5:
                modop()
            case 6:
                expop()
            case 7:
                print("Thx for Using This Program")
                break
            case _:
                print("Ur Selection of Operation is Wrong--Try Again")
    else:
        print("Ur Selection of Operation is Wrong--Try Again")