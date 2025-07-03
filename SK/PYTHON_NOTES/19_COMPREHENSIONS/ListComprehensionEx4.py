#Program for Demonstrating the List Comprehension
#ListComprehensionEx4.py
print("Enter List of Values separated by comma:")
lst=[  float(val)   for val in input().split(",") ]
print("content of list=",lst)