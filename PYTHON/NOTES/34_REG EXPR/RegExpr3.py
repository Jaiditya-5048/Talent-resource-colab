#RegExpr3.py-----finditer()
import re
gd="Python is an oop lang.Python is also Fun prog lang"
sp="an"
matres=re.finditer(sp,gd) # here matres is an object of type <class 'callable_iterator'>
for mat in matres: # Here mat is an object of type <class, re.match>
	print("start Index:{}\tEnd Index:{}\tValue:{}".format(mat.start(),mat.end(),mat.group()))