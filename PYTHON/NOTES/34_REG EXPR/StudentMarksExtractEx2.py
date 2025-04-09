#write a python program which will extract to the marks from givem text--with Reg Expr
#StudentMarksExtractEx2.py
import re
gd="Nihal got 66 marks, Pathyusha got 55 marks , Rajeswari got 44 marks , Astha got 54 marks , Sindhuja got 48 marks and Rossum got 77 marks and kvr got 11 marks and Mamatha got 67 marks"
markslist=re.findall(r"\d{2}",gd)
print("----------------------------------")
print("Marks of Students")
print("----------------------------------")
for marks in markslist:
	print("\t{}".format(marks))
print("----------------------------------")