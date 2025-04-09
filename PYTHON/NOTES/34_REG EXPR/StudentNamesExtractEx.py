#write a python program which will extract name of the people form the given line of text--without Reg Expr
#StudentNamesExtractEx.py
import re
gd="Nihal got 66 marks, Pathyusha got 55 marks , Rajeswari got 44 marks , Astha got 54 marks , Sindhuja got 48 marks and Rossum got 77 marks and Kvr got 11 marks"
words=gd.split()
for word in words:
	if(word[0].isupper()):
		print(word)
	
