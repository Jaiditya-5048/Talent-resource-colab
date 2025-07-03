#Program for demonstrating the need of generators
#GenEx1.py
def kvrange(val):
		i=1
		while(i<=val):
			yield i
			i=i+1

#Main Program
r=kvrange(5) # Function Call which biuld generator object
#here r is an object of generator class
#to get the data from generator, we have a general pre-defined function called next()
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
#print(next(r))----gives StopIteration
print("---------------OR-------------------")
r1=kvrange(8)
for val in r1:
	print(val)
#print(next(r1))---------gives StopIteration
print("---------------OR-------------------")
r2=kvrange(10)
while(True):
	try:
		print(next(r2))
	except StopIteration:
		break
