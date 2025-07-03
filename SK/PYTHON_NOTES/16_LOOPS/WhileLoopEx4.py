#Program for Generating Even Numbers  Within N Numbers where N is +Ve
#WhileLoopEx4.py
n=int(input("Enter How many Even Numbers u want to Generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print('-'*50)
    print("Numbers within:{}".format(n))
    print('-' * 50)
    i=2
    while(i<=n):
        print(i)
        i+=2 # here += is called Short Hand + Operator
    else:
        print()
        print('=' * 50)
print("Program execution completed")


