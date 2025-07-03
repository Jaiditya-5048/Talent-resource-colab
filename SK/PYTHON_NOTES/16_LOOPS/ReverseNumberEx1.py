#Program for Onbtaining Reverse of a Given number without str slicing
#ReverseNumberEx1.py
n=int(input("Enter an Inetger Number:")) # 2345
if(n<0):
    print("Invalid Input:")
else:
    rn=0
    while(n>0):
        r=n%10
        rn=rn*10+r
        n=n//10
    else:
        print("Reversed Number=",rn)
