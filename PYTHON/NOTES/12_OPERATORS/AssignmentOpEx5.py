#Program for Swapping Two Integer Values by using Assignment Operator
#AssignmentOpEx5.py
print("Enter Two Integer Values")
a,b=int(input()),int(input()) # Multi Line Assigment
print("-"*50)
print("Original value of a:{}".format(a))
print("Original value of b:{}".format(b))
print("-"*50)
#Swapping Logic by using Single Line Assigment Operator
a=a*b
b=a//b
a=a//b
print("Swapped value of a:{}".format(a))
print("Swapped value of b:{}".format(b))
print("-"*50)

