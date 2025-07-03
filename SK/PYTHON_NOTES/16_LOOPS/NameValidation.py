#Program for Validation of Name
#NameValidation.py
name=input("Enter Ur Name:")# name="Guido Van Ro3ssum"
words=name.split() # words=[Gu2ido, Van , Rossum]
res="Valid Name"
for word in words:
    if(not word.isalpha()):
        res="Invalid Name"
        break
print("{} is {}".format(name,res))

