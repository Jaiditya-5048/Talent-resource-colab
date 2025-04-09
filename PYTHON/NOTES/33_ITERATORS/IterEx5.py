#Program for Converting Iterable Object into Iterator object by using iter()
#IterEx5.py
x="PYTHON"
print("Type of x=",type(x)) #  <class 'str'>
#Convert x type into Iterator type by suign iter()
itr=iter(x)
print("Type of itr=",type(itr)) # <class 'str_ascii_iterator'>
for val in itr:
	print(val)
#print(next(itr))-------gives StopIteration