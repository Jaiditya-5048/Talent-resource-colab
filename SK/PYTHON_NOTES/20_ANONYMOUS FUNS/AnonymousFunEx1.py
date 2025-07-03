#AnonymousFunEx1.py
def sumop(a, b):
    return a + b

addop=lambda a,b: a+b # Anonymous Function

#Main Program
print("Type of sumop=",type(sumop)) # <class 'function'>
res=sumop(100,200)
print("Sum by Using Normal Function=",res)
print("----------------------------------------")
print("type of addop=",type(addop))#<class 'function'>
res1=addop(1000,2000)
print("Sum by Using Anonymous Function=",res1)