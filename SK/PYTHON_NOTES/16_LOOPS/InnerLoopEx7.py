#Program for generating Multiplication tables for Random list of values
#InnerLoopEx7.py
lst=[12,-19,18,25,-5,15,-5,0,3]
for num in lst:
    if(num<=0):
        print("{} is Invalid Input:".format(num))
    else:
        print("-"*50)
        print("Mul Table for :{}".format(num))
        print("-" * 50)
        for i in range(1,11):
            print("\t{} x {}={}".format(num,i,num*i))
        else:
            print("-" * 50)
