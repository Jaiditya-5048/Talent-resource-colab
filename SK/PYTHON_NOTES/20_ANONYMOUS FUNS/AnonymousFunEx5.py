#write a python program which will accept list of values
# and find the max and min by using anonymous functions.
#AnonymousFunEx4.py
def kvrmax(lst):
    maxv=lst[0]
    for val in lst:
        if(val>maxv):
            maxv=val
    return maxv
def kvrmin(lst):
    minv=lst[0]
    for val in lst:
        if(val<minv):
            minv=val
    return minv

findmax=lambda x:kvrmax(x) # Anonymous Functions
findmin=lambda x:kvrmin(x)  # Anonymous Functions

#Main Program
print("Enter List of Values separated by space:")
lst=[float(val) for val in input().split()] # List Comprehension
print("Given List of Values=",lst)
maxv=findmax(lst) # Anonymous Function call
minv=findmin(lst) #  Anonymous Function call
print("Maximum Value={}".format(maxv))
print("Minimum Value={}".format(minv))