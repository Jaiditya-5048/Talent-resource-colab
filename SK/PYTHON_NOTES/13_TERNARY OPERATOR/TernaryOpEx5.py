#write a python program which will accept two numerical values
# and decide the biggest among them and check for equality
#TernaryOpEx5.py
val1=float(input("Enter First Value:")) # Val1=10
val2=float(input("Enter Second Value:")) # Val2=10
res="Both Values Equal" if val1==val2 else val1 if val1>val2 else val2
print("max({},{})={}".format(val1,val2,res))