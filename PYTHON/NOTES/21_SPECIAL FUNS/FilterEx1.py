#Program for Demonstrating filter() for obtaining +ve Values only
#FilterEx1.py
def posfun(val): # Normal Function definition
	if(val>0):
		return True
	else:
		return False


#main Program
lst=[10,-2,20,-3,30,-4,-5,60,50,-7,0,12]

filterobj=filter(posfun,lst) # Here posfun is a Normal function and lst is an Iterable Object
#here filterobj is an object of <class, 'filter'>
#print("content of filterobj=",filterobj)--<filter object at 0x0000019BD86CA620>
#Convert filter object into either list,tuple,set..etc
pslist=list(filterobj)
print("Original Elements=",lst)
print("Possitive Elements=",pslist)