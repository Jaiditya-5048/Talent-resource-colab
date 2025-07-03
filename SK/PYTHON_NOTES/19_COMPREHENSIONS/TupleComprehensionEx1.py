#Program for Demonstrating the Tuple Comprehension
#TupleComprehensionEx1.py
tpl=(10,2,13,4,-5,11,-6,18)
sqlist=(val**2  for val in tpl)   #----------here  sqlist is an object of <class, 'generator>   but not Tuple
#Convert generator object into tuple by using type casting concept
tpl=tuple(sqlist)
print(tpl,type(tpl))