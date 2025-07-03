#Program for Validation of Name
#NameValidationalternate.py
while True:
    name=input("Enter Ur Name:")# name="Guido Van Ro3ssum"
    words=name.split() # words=[Gu2ido, Van , Rossum]
    res=True
    for word in words:
        if(not word.isalpha()):
            res=False
            break
    if(res):
        print("{} is Valid Name:".format(name))
        break
    else:
        print("\t\t{} is In Valid Name:".format(name))

