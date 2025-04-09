#Program for Demonstrating filter() for obtaining +ve Values only
#FilterEx3.py
lst=[int(val) for val in input("Enter List of Values separated by space:").split()]
pslist=list(filter( lambda val: val>0 , lst))
nglist=tuple(filter(lambda val:val<0,lst))
print("------------------------------------------------------")
print("Given List of Values:",lst)
print("Possitive Elements=",pslist)
print("Negative Elements=",nglist)
print("------------------------------------------------------")