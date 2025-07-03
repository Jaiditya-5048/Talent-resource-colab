#Program for Reading List of Value dynamically and display
#ReadDisplayValuesEx2.py
lst=[]
while("KVR"):
    val=input("Enter a Value (Press @ to Stop):")
    if(val=="@"):
        break
    else:
        lst.append(float(val))
print("Content of list=",lst)