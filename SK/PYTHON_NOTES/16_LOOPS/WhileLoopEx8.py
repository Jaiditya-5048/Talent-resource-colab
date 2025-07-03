#Program for Finding sum of Digits of a Given Number--Logic-2
#WhileLoopEx8.py
num=int(input("Enter a Number for Its Digits Sum:")) # Num=3278
if(num<0):
    print("Invalid Input")
else:
    sumvals=0
    i=0
    s=str(num)
    while(i<len(s)):
        sumvals=sumvals+int(s[i])
        i=i+1
    else:
        print("sum of digits({})={}".format(s,sumvals))
        print("================OR======================")
        s=0
        for val in str(num):
            s=s+int(val)
        else:
            print("sum of digits({})={}".format(num,s))
