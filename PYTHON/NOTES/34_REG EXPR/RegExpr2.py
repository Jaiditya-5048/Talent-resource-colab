#RegExpr2.py-----search()
import re
gd="Python is an oop lang.Python is also Fun prog lang"
sp="Python"
mat=re.search(sp,gd) # x-- is of Type <class, re.match>  OR <class,NoneType>
if(mat!=None):# here mat is an object of class Match
	print("Search is Sucessful")
	print("Start Index:{}".format(mat.start()))
	print("End Index:{}".format(mat.end()))
	print("Matched Value:{}".format(mat.group()))
else: #here mat is an object of NoneType
	print("Search is Un-Sucessful")
	print("'{}' does not Exist in Given Data".format(sp))

	
