#Program for finding Max and Min from List of Value dynamically
#FindMaxMinEx.py
lst=[]
print("Enter a Value (Press ! to Stop):")
while(True):
    val=input()
    if(val=="!"):
        break
    else:
        lst.append(float(val))
print("Content of list=",lst) # [10.0, 2.0, 23.0, 5.0, -1.0, 26.0]
#Code for Finding Max and Min Values
maxv=minv=lst[0]
for val in lst:
    if(val>maxv):
        maxv=val
    elif(val<minv):
        minv=val
else:
    print("Max({})={}".format(lst,maxv))
    print("Min({})={}".format(lst,minv))



