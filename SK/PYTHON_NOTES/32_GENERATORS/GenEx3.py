#Program for demonstrating the need of generators
#GenEx3.py
def kvrange(beg,end,step=1):
	while(beg<=end):
		yield beg
		beg=beg+step


#Main Program
r1=kvrange(10,20,2) # # Function Call which biuld generator object
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