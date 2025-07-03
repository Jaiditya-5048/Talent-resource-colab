#Program for Reading List of Value dynamically and display
#ReadDisplayValuesEx3.py
lst=[]
print("Enter a Value (Press ! to Stop):")
while(True):
    val=input()
    if(val=="!"):
        break
    else:
        lst.append(float(val))
print("Content of list=",lst)