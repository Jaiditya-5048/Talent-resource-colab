#write a python program which will extract name of the people form the given line of text--with Reg Expr
#StudentNamesExtractEx1.py
import re
gd="Nihal got 66 marks, Pathyusha got 55 marks , Rajeswari got 44 marks , Astha got 54 marks , Sindhuja got 48 marks and Rossum got 77 marks and kvr got 11 marks and Mamatha got 67 marks"
nameslist=re.findall("[A-Z][a-z]+",gd)
print('------------------------------------------')
print("\tNames List")
print('------------------------------------------')
for name in nameslist:
	print("\t{}".format(name))
print('------------------------------------------')