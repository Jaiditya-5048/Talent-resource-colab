#Program for Deciding the type of value by using Functions
#ValueType.py
def valuetype(obj):
    if(type(obj)==int):
        print("{} is Integer Value:".format(obj))
    elif(type(obj)==float):
        print("{} is Float Value:".format(obj))
    elif (type(obj) == bool):
        print("{} is Bool Value:".format(obj))
    elif (type(obj) == complex):
        print("{} is complex Value:".format(obj))
    elif (type(obj) == str):
        print("{} is String Value:".format(obj))
    elif (type(obj) == bytes):
        print("{} is bytes Value:".format(obj))
    elif (type(obj) == bytearray):
        print("{} is Bytearray Value:".format(obj))
    elif (type(obj) == range):
        print("{} is range Value:".format(obj))
    elif (type(obj) == list):
        print("{} is list Value:".format(obj))
    elif (type(obj) == tuple):
        print("{} is tuple Value:".format(obj))
    elif (type(obj) == set):
        print("{} is set Value:".format(obj))
    elif (type(obj) == frozenset):
        print("{} is frozenset Value:".format(obj))
    elif (type(obj) == dict):
        print("{} is dict Value:".format(obj))
    else:
        print("{} is NoneType Value:".format(obj))
#Main Program
a=10
valuetype(a) # Function Call
b=2.3
valuetype(b) # Function Call
c=True
valuetype(c) # Function Call
d=2+3j
valuetype(d) # Function Call
s="Python"
valuetype(s)
b=bytes([10,20,30,40])
valuetype(b)
ba=bytearray([10,20,30,40,50,123])
valuetype(ba)
r=range(10,20,2)
valuetype(r)
lst=[10,"RS"]
valuetype(lst)
tpl=(10,20,30)
valuetype(tpl)
st={10,20,30,40,10}
valuetype(st)
fst=frozenset([10,10,20,20])
valuetype(fst)
d={10:1.2,20:1.3}
valuetype(d)
x=None
valuetype(x)
