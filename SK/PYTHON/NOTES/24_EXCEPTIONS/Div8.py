#Program for Performing Division of Two Numbers
#Div8.py-----This Program Defined by KVR Programmer in the Year 2024 Aug 28th
# after 5 Years This program may for for Modification or Updation
#At that point of time, Ashis is the new Programmer--2029 Aug , May add new Statement and new statement may generate exception and KVR want to handle such type unknown future exceptions at this point of time.
try:
	print("Program Execution Started:")
	a=input("Enter First Number:")
	b=input("Enter Second Number:")
	x=int(a) #---------------------Exception generated statement----ValueError
	y=int(b) #---------------------Exception generated statement----ValueError
	z=x/y #---------------------Exception generated statement------ZeroDivisionError
	s="PYTHON"
	print(s[50])
except ZeroDivisionError:   # Specific Except block
	print("\tDon't Enter Zero for Den......")
except ValueError: # Specific Except block
	print("\tDon't enter alnums,strs and symbols")
except BaseException as e: # default except block
	print("\tooops Some thing went wrong!!!",e)
else:
	print("-----else block------")
	print("First Number:",x)
	print("Second Number:",y)
	print("Div={}".format(z))
finally:
	print("Program Execution Ended--finally block:")


