#Program for Deciding whether the word is Palindrome or not
#TernaryOpEx3.py
word=input("Enter Any Word:") # REEL
res= "Not Palindrome" if word!=word[::-1] else "Palindrome"
print("{} is {}".format(word,res))