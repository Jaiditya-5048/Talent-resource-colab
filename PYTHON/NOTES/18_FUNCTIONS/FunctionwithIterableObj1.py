#FunctionwithIterableObj1.py
def dispValues(obj): # here lst is called Formal Parameter
    print("-----------------------------")
    print("Type of Values:",type(obj))
    for val in obj:
        print(val)
    print("-----------------------------")
def dispValues1(obj): # here lst is called Formal Parameter
    print("-----------------------------")
    print("Type of Values:",type(obj))
    for key,val in obj.items():
        print("{}--->{}".format(key,val))
    print("-----------------------------")
#main Program
lst=[10,"Rossum",45.67,True,2+3j]
dispValues(lst) # Function call
tpl=(10,20,30,40,50,60)
dispValues(tpl)
st={10,"Travis",45.67,False,10}
dispValues(st)
s="PYTHON"
dispValues(s)
d={10:1.2,20:3.4,30:4.5,40:6.7}
dispValues1(d)
