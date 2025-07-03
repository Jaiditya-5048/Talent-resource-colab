#Program for Performing Division of Two Numbers
#Div3.py
try:
	print("Program Execution Started:")
	a=input("Enter First Number:")
	b=input("Enter Second Number:")
	x=int(a) #---------------------Exception generated statement----ValueError
	y=int(b) #---------------------Exception generated statement----ValueError
	z=x/y #---------------------Exception generated statement------ZeroDivisionError
except (ZeroDivisionError,ValueError): # Multi Exception Handling block
	print("\tDon't Enter Zero for Den......")
	print("\tDon't enter alnums,strs and symbols")
else:
	print("-----else block------")
	print("First Number:",x)
	print("Second Number:",y)
	print("Div={}".format(z))
finally:
	print("Program Execution Ended--finally block:")


