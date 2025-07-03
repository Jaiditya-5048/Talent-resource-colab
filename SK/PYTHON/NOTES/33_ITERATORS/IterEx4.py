#Program for Converting Iterable Object into Iterator object by using iter()
#IterEx4.py
x={10:1.2,20:2.3,30:4.5,40:1.2}
print("Type of x=",type(x)) #  <class 'dict'>
#Convert x type into Iterator type by suign iter()
itr=iter(x)
print("Type of itr=",type(itr)) # <class 'dict_keyiterator'>
for val in itr:
	print("{}-->{}".format(val,x.get(val)))
#print(next(itr))-------gives StopIteration