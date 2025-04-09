#Program for Demonstrating filter() for obtaining +ve Values only
#FilterEx2.py

posfun=lambda x: x>0 #Anonymous function
negfun=lambda a: a<0 #Anonymous function
#main Program
lst=[10,-2,20,-3,30,-4,-5,60,50,-7,0,12]
pslist=tuple(filter(posfun,lst))
nglist=tuple(filter(negfun,lst))
print("Original Elements=",lst)
print("Possitive Elements=",pslist)
print("Negative Elements=",nglist)