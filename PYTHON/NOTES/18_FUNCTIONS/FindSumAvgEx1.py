#Program for Finding Suma and Average of List of Values by using Functions
#FindSumAvgEx1.py
def  readvalues():
    nov=int(input("Enter How Many Values u want to Enter:"))
    if(nov<=0):
        return []  # OR return list()
    else:
        lst=[] # empty list for storing values
        for i in range(1,nov+1):
            val=float(input("Enter {} Value:".format(i)))
            lst.append(val)
        return lst

def findsumavg(lst):
    if(len(lst)==0):
        print("List is empty can't find sum and avg")
    else:
        print("="*50)
        print("List of Values:")
        print("=" * 50)
        #lst=[10,20,30,40]
        s=0
        for val in lst:
            print(val)
            s=s+val
        else:
            print("=" * 50)
            print("Sum=",s)
            print("Avg=",s/len(lst))
            print("=" * 50)

#Main Program
lst=readvalues() # Function call
findsumavg(lst) # Functio Call