#write a python program which will extract to the marks from givem text--without using Reg Expr
#StudentMarksExtractEx1.py
import re
gd="Nihal got 66 marks, Pathyusha got 55 marks , Rajeswari got 44 marks , Astha got 54 marks , Sindhuja got 48 marks and Rossum got 77 marks and kvr got 11 marks and Mamatha got 67 marks"
words=gd.split()
for word in words:
	if(len(word)==2) and (word.isdigit()):
		print(word)
