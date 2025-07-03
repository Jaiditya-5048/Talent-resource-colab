#write a python program which will accept a word and decide
# whether it is palandendrum or not by using ananymous fun
#AnonymousFunEx3.py
palindrome=lambda n:"Palindrome" if n==n[::-1] else "Not Palindrome"

#Main Program
n=input("Enter Value / word:")
res=palindrome(n) # Function Call
print('{} is {}'.format(n,res))