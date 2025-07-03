#Program for Sorting List of Names by using functions
#SortNamesEx1.py
def readnames():
    print("Enter List of Names (Press @ to stop):")
    nameslist=[]
    while(True):
        name=input()
        if(name!="@"):
            nameslist.append(name)
        else:
            break
    sortnames(nameslist)  # Function Call in Function Definition
def sortnames(nameslist):
    if(len(nameslist)==0):
        print("List is empty and can't sort")
    else:
        print("-" * 50)
        print("Original List of Names:")
        print("-"*50)
        for name in nameslist:
            print("\t{}".format(name))
        print("-" * 50)
        print("Ascending Order of Names:")
        nameslist.sort()
        for name in nameslist:
            print("\t{}".format(name))
        print("-" * 50)
        print("Decending Order of Names:")
        nameslist.sort(reverse=True)
        for name in nameslist:
            print("\t{}".format(name))
        print("-" * 50)


#main Program
readnames() # function call
