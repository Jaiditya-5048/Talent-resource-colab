#Program for Reading List of Value dynamically and display
#ReadDisplayValuesEx1.py
noe=int(input("How Many Elements u want Enter:"))
if(noe<=0):
    print("{} is Invalid Input".format(noe))
else:
    lst=[] # OR lst=list()
    for i in range(1,noe+1):
        val=float(input("Enter {} Value:".format(i)))
        lst.append(val)
    else:
        print("List of Elements")
        for val in lst:
            print("\t{}".format(val))