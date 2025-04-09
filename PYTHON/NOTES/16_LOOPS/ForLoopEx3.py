#ForLoopEx3.py
d={10:"Python",20:"C",30:"C++",40:"HTML",50:"DSA"}
for k in d:
    print("{}---->{}".format(k,d[k]))
print("-----------------------------")
for k in d.keys():
    print("{}--->{}".format(k,d.get(k)))
print("-----------------------------")
for k,v in d.items():
    print("{}---->{}".format(k,v))
print("-------------------------------")
print("By using while loop")
print("-------------------------------")
ks=list(d.keys())
i=0
while(i<len(ks)):
    print("{}--->{}".format(ks[i],d[ks[i]]))
    i=i+1
print("-------------------------------")
print("By using while loop")
print("-------------------------------")
ks=list(d.keys())
i=0
while(i<len(ks)):
    print("{}--->{}".format(ks[i],d.get(ks[i])))
    i=i+1
print("-------------------------------")