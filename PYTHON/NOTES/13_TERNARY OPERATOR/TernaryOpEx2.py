#Program for accepting a Numerical Inetegr values
# and decide whether it is Even or odd
#TernaryOpEx2.py
n=int(input("Enter any Integer Value:"))
result = "Even"  if  n%2==0  else  "Odd"
print("{} is {}".format(n,result))