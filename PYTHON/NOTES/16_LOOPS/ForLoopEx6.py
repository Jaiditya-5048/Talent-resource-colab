#Program for Finding Sum of List of Numerical values.
#ForLoopEx6.py
lst=[10,20,30,12,15,30,56]
s=0
for val in lst:
    print("\t{}".format(val))
    s+=val
else:
    print("Sum=",s)