#Program for Converting Iterable Object into Iterator object by using iter()
#IterEx3.py
x={10,"RS",34.56,True,2+3j}
print("Type of x=",type(x)) #  <class 'set'>
#Convert x type into Iterator type by suign iter()
itr=iter(x)
print("Type of itr=",type(itr)) # <class 'set_iterator'>
for val in itr:
	print(val)
#print(next(itr))-------gives StopIteration