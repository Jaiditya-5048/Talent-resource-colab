#Program for Demonstrating the List Comprehension
#ListComprehensionEx5.py
print("Enter List of Values separated by comma:")
lst=[ int(val)  for val in input().split(",")   if not  val.lstrip().startswith("-") ]
print("List of +ve Values=",lst)
