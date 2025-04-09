#Program for Reading List of Value dynamically and find sum and avg without using sum()
#SumAvgEx2.py
noe=int(input("How Many Elements u want Enter:"))
if(noe<=0):
    print("{} is Invalid Input".format(noe))
else:
    lst=[] # OR lst=list()
    for i in range(1,noe+1):
        val=float(input("Enter {} Value:".format(i)))
        lst.append(val)
    else:
        print("List of Elements=",lst) # [10.0, 20.0, 30.0, 40.0, 50.0]
        s=0
        for val in lst:
            s=s+val
        else:
            print("Sum={}".format(round(s,2)))
            print("Avg={}".format(round(s/len(lst),2)))
