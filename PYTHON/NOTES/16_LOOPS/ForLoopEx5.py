#Program for Finding Sum of N Natrual Numbers where N is +Ve
#ForLoopEx5.py
n=int(input("Enter How Many Natural Numbers Sum u want to Find:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    s,ss,cs=0,0,0
    print("-------------------------------")
    print("NatNums\t\tSquares\t\tCubes")
    print("-------------------------------")
    for i in range(1,n+1):
        print("\t{}\t\t{}\t\t\t{}".format(i,i**2,i**3))
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
    else:
        print("-------------------------------")
        print("\t{}\t\t{}\t\t\t{}".format(s,ss,cs))
        print("-------------------------------")
