#Program for Adding Two List Elements and place them in another List by using map()
#MapEx4.py
lst1=[10,20,30,40]
lst2=[100,200,300,400]

lst3=list(map( lambda k,v : k+v, lst1,lst2))

print("List1=",lst1)
print("List2=",lst2)
print("List3=",lst3)