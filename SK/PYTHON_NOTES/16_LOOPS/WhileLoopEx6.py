#Program for Finding Factorial of a Number
#WhileLoopEx6.py
n=int(input("Enter a Number for Finding Factorial of a Number:")) # n=4
if(n<0):
    print("We can't cal Factorial for {} Number".format(n))
else:
    tn=n #We are Preverving Original in Temp Var
    fact=1
    while(n>0):
        fact=fact*n
        n=n-1
    else:
        print("{}!={}".format(tn,fact))

#NOTE: Student must do he above program by using for loop