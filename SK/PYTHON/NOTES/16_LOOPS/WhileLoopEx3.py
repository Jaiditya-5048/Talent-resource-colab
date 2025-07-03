#Program for generating n to 1 where n is +Ve
#WhileLoopEx3.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("{} is Invalid input".format(n))
else:
    print('-' * 50)
    print("Numbers within:{}".format(n))
    print('-' * 50)
    while(n>0):
        print(n,end=" ")
        n=n-1
    else:
        print()
        print('=' * 50)