#Program for Finding Suma and Average of List of Values by using Functions
#FindSumAvgEx3.py
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
def findsum(lst):
    if(len(lst)==0):
        print("List is empty Can't find sum")
    else:
        s=sum(lst)
        print("Sum={}".format(s))
        print("Avg={}".format(s/len(lst)))
#Main Program
lst=readvalues() # Function call
findsum(lst) # Functio Call
