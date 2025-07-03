#Program for Performing Division of Two Numbers
#Div5.py---This Program is not recommeded to write only with default except block.
try:
	print("Program Execution Started:")
	a=input("Enter First Number:")
	b=input("Enter Second Number:")
	x=int(a) #---------------------Exception generated statement----ValueError
	y=int(b) #---------------------Exception generated statement----ValueError
	z=x/y #---------------------Exception generated statement------ZeroDivisionError
except:  # Default except block
	print("\tooops Some thing went wrong!!!")
else:
	print("-----else block------")
	print("First Number:",x)
	print("Second Number:",y)
	print("Div={}".format(z))
finally:
	print("Program Execution Ended--finally block:")


