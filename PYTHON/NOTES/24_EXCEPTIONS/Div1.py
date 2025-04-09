#Program for Performing Division of Two Numebrs
#Div1.py
print("Program Execution Started:")
a=input("Enter First Number:")
b=input("Enter Second Number:")
x=int(a) #---------------------Exception generated statement----ValueError
y=int(b) #---------------------Exception generated statement----ValueError
print("First Number:",x)
print("Second Number:",y)
z=x/y #---------------------Exception generated statement------ZeroDivisionError
print("Div={}".format(z))
print("Program Execution Ended:")