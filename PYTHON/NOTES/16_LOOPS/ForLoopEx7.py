#Program for Finding product of N Natural Numbers where n is +ve
#ForLoopEx7.py
n=int(input("Enter Hor Many Natural Numbers Product u want to Find:"))
if(n<=0):
    print("{} is Invalid".format(n))
else:
    prod=1 #
    for i in range(1,n+1):
        print("\t{}".format(i))
        prod=prod*i # OR  prod*=i
    else:
        print("Product=",prod)