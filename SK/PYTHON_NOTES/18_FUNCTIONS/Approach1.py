#Write a Python Program " To Add Two Number " by using functions.
#Approach1.py
def addop(k,v):
    print("I am Inside of Function Body")
    r=k+v # Here 'r' is called Local Variable
    return r

#Main Program
print("type of addop=",type(addop))
print("------------------------------------")
print("I am before Function call")
result=addop(10,20) # Function Call
print("Sum=",result)
print("I am after Function call")
print("----------------------------")
res=addop(-10,-20) # Function call
print("sum=",res)
print("----------------------------")
r=addop(100,-200) # Function call
print("sum=",r)
