#Program for demonstrating the need of generators
#GenEx2.py
def kvrange(beg,end):
	while(beg<=end):
		yield beg
		beg=beg+1


#Main Program
r1=kvrange(10,20) # # Function Call which biuld generator object
while(True):
	try:
		print(next(r1))
	except StopIteration:
		break
print("---------------------------------------")
r2=kvrange(100,106) # # Function Call which biuld generator object
for val in r2:
	print(val)
print("---------------------------------------")