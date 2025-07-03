#Program for Finding sum of Digits of a Given Number--Logic-1
#WhileLoopEx7.py
num=int(input("Enter a Number for Its Digits Sum:"))
if(num<0):
    print("Invalid Input")
else:
    s=0
    tn=num
    while(num>0):
        r=num%10
        s=s+r
        num=num//10
    else:
        print("sum of digits({})={}".format(tn,s))
#Student must try with for loop