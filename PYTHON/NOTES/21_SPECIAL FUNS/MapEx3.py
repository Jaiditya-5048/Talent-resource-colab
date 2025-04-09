#Program for Demonstrating the map()
#MapEx3.py
print("Enter List of Salaries of employee separated by space:")
oldsallist=[float(sal) for sal in input().split()  if float(sal)>0 ]
newsal=list(map(lambda sal: sal*1.5,oldsallist))
print("--------------------------------------------------")
print("Old Salary\tNew Salary")
print("--------------------------------------------------")
for ol,nl in zip(oldsallist,newsal):
	print("\t{}\t{}".format(ol,nl))
print("--------------------------------------------------")