#Program for Accepting List of Values and find OR Get Unique Values.
#UniueElementsEx1.py
noe=int(input("How Many Elements u want Enter:"))
if(noe<=0):
    print("{} is Invalid Input".format(noe))
else:
    lst=[] # OR lst=list()
    for i in range(1,noe+1):
        val=float(input("Enter {} Value:".format(i)))
        lst.append(val)
    else:
        print("List of Elements=",lst)# [10.0, 20.0, 10.0, 30.0, 20.0]
        uqlist=list() # creating an empty list for storing Unique Vals
        for val in lst:
            if(val in uqlist):
                continue
            uqlist.append(val)
        else:
            print("List of Unique Elements")
            print(uqlist)









