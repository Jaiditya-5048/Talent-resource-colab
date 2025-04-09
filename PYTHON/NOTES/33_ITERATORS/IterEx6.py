#Program for Converting Iterable Object into Iterator object by using iter()
#IterEx6.py
x=range(10,31,5)
print("Type of x=",type(x)) #  <class 'range'>
#Convert x type into Iterator type by suign iter()
itr=iter(x)
print("Type of itr=",type(itr)) # <class 'range_iterator'>
for val in itr:
	print(val)
#print(next(itr))-------gives StopIteration