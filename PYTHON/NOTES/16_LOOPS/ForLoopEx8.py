#Program for Finding Factorial of a Number
#ForLoopEx8.py
n=int(input("Enter a Number for Finding Factorial of a Number:"))
if(n<0):
    print("We can't cal Factorial for {} Number".format(n))
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    else:
        print("Factorial({})={}".format(n,fact))

#Note: Student must do the above Program with while loop