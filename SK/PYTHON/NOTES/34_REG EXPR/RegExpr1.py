#RegExpr1.py---findall()
import re
gd="Python is an oop lang.Python is also Fun prog lang"
sp="Python"
res=re.findall(sp,gd) # res=["Python","Python"] here res is type <class, list>
print("Result=",res) # res=["Python","Python"]
print("Number of occurences =",len(res))
