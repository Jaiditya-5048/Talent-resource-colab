#Program for Onbtaining Reverse of a Given number
#ReverseNumberEx1.py
n=input("Enter an Inetger Number:") # 2345
if(n.isdigit()):
    if(int(n)<0):
        print("Invalid Input:")
    else:
        s=""
        for val in n[::-1]:
            s=s+val
        else:
            print("Reversed Number=",s)
else:
    print("Reversed Number=", n[::-1])




