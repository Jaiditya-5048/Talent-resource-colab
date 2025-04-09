#Program for Generating Mul Table
#Table.py<----File Name and acts as Module Name
def table():
	n=int(input("Enter a Number for Generating Mul table:"))
	if(n<=0):
		print("{} is invalid input".format(n))
	else:
		print("----------------------------------------------------")
		print("Mul Table for {}".format(n))
		print("----------------------------------------------------")
		for i in range(1,11):
			print("\t{} x {}={}".format(n,i,n*i))
		print("----------------------------------------------------")

