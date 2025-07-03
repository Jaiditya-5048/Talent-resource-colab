#Program for Finding Sum of N Natrual Numbers where N is +Ve
#ForLoopEx4.py
n=int(input("Enter How Many Natural Numebrs Sum u want to find:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("Sum of First {} Natural Numebrs:".format(n))
    print("-" * 50)
    i=1
    s=0 # Additive Identity
    # Additive Identity is used here for Accumutaling Sum of i values
    while(i<=n):
        print("\t\t\t{}".format(i))
        s=s+i  # Accumutaling Sum of i values
        i=i+1
    else:
        print("-" * 50)
        print("Sum of {} Natural Number={}".format(n,s))
        print("-" * 50)
        print("=================================================")
        print("By using for loop")
        print("=================================================")
        n = int(input("Enter How Many Natural Numebrs Sum u want to find:"))
        if (n <= 0):
            print("{} is Invalid Input".format(n))
        else:
            print("-" * 50)
            print("Sum of First {} Natural Numbers:".format(n))
            print("-" * 50)
            s=0 # Additive Identity
            for i in range(1,n+1):
                print("{}".format(i),end=" ")
                s+=i
            else:
                print()
                print("-" * 50)
                print("Sum of {} Natural Number={}".format(n, s))
                print("-" * 50)
