#Program for Adding Two List Elements and place them in another List by using map()
#MapEx7.py
print("Enter List of Values for First List Separated by Space:")
lst1=[int(val) for val in input().split()] # Sal=[1000,2000,3000,4000,5000,6000]
print("Enter List of Values for Second List Separated by Space:")
lst2=[int(val) for val in input().split()] # com=[500,250,100]
if( len(lst1)>len(lst2) ):
	for i in range(len(lst1)-len(lst2)):
		lst2.append(0)
elif(len(lst2)>len(lst1)):	
	for i in range(len(lst2)-len(lst1)):
		lst1.append(0)
#Adding List1 and List2 Elements by using Map
lst3=list(map(lambda k,v:k+v,lst1,lst2))
print("="*50)
print("\tList-1\tList-2\tSumList")
print("="*50)
for v1,v2,v3 in zip(lst1,lst2,lst3):
	print("\t{}\t{}\t{}".format(v1,v2,v3))
print("="*50)
