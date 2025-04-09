#write a python program which will accept list of values
# and find the max and min by using anonymous functions.
#AnonymousFunEx4.py

findmax=lambda x:max(x)
findmin=lambda x:min(x)

#Main Program
print("Enter List of Values separated by space:")
lst=[float(val) for val in input().split()]
print("Given List of Values=",lst)
maxv=findmax(lst) # Function call
minv=findmin(lst) # Function call
print("Maximum Value={}".format(maxv))
print("Minimum Value={}".format(minv))