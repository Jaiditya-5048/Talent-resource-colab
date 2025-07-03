#write a python program which will extract  the names and marks from givem text--with Reg Expr
#StudentNamesMarksExtractEx.py
import re
gd="Nihal got 66 marks, Pathyusha got 55 marks , Rajeswari got 44 marks , Astha got 54 marks , Sindhuja got 48 marks and Rossum got 77 marks and kvr got 11 marks and Mamatha got 67 marks"
nameslist=re.findall("[A-Z][a-z]+",gd)
markslist=re.findall(r"\d{2}",gd)
print("----------------------------------")
print("\tNmes\t\tMarks")
print("----------------------------------")
for names,marks in zip(nameslist,markslist):
	print("\t{}\t\t{}".format(names,marks))
print("----------------------------------")