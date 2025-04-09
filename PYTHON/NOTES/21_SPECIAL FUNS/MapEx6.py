#Program for Concatinating Two List Elements and place them in another List by using map()
#MapEx6.py
print("Enter List of Words for First List Separated by Space:")
lst1=[val for val in input().split()]
print("Enter List of Words for Second List Separated by Space:")
lst2=[str(val) for val in input().split()]
lst3=list(map( lambda k,v : k+" "+v, lst1,lst2))
print("="*50)
print("\tList-1\tList-2\tConCatList")
print("="*50)
for v1,v2,v3 in zip(lst1,lst2,lst3):
	print("\t{}\t{}\t{}".format(v1,v2,v3))
print("="*50)
