#Program for Demonstrating the List Comprehension
#ListComprehensionEx6.py
print("Enter List of Values separated by space:")
lst=[ int(val)  for val in input().split()   if int(val)>0 ]
print("List of +ve Values=",lst)

print("Enter List of Values separated by space:")
lst=[ int(val)  for val in input().split()   if int(val)<0 ]
print("List of -ve Values=",lst)
