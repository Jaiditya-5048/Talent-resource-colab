#Program for Demonstrating the map()
#MapEx2.py
hike=lambda sal:sal+sal*50/100  # OR  hike=lambda sal:sal*1.5

#Main Program
oldsallist=[100,200,300,400,500]
newsal=list(map(hike,oldsallist))
print("--------------------------------------------------")
print("Old Salary\tNew Salary")
print("--------------------------------------------------")
for ol,nl in zip(oldsallist,newsal):
	print("\t{}\t{}".format(ol,nl))
print("--------------------------------------------------")