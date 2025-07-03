#Program for Demonstrating the map()
#MapEx1.py
def hike(sal):
	return (sal+sal*50/100)

#Main Program
oldsallist=[100,200,300,400,500]
mapobj=map(hike,oldsallist)
print("type of mapobj=",type(mapobj))# type of mapobj= <class 'map'>
newsal=list(mapobj)
print("Old Salary List=",oldsallist)
print("New Salary List=",newsal)