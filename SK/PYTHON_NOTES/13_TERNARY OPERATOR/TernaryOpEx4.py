#Write a python program which will accept any numerical value and decide
# whether it is positive or negative or 0 (zero).
#TernaryOpEx4.py
n=float(input("Enter a Number:")) # n= 100   -100     0
res="+VE" if n>0 else "-VE" if n<0 else "ZERO"
print("{} is {}".format(n,res))