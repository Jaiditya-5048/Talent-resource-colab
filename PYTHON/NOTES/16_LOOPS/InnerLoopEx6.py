#Program for Generating 1 to N Multiplication Tables
#InnerLoopEx6.py
n=int(input("Enter How Many Mul Tables u want:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    for num in range(1,n+1): # Outer loop supply the number
        print("-"*50)
        print("Mul Table for {}".format(num))
        print("-" * 50)
        for i in range(1,11):# inner loop generate mul table for number supplied by outer loop
            print("\t{} x {} = {}".format(num,i,num*i))
        else:
            print("-" * 50)
