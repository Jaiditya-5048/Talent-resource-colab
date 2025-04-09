#Program for Generating 1 to N Numbers where N is +Ve
#WhileLoopEx2.py
n=int(input("Enter How many Numbers u want to Generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print('-'*50)
    print("Numbers within:{}".format(n))
    print('-' * 50)
    i=1
    while(i<=n):
        print(i)
        i+=1 # here += is called Short Hand + Operator
    else:
        print()
        print('=' * 50)
print("Program execution completed")


