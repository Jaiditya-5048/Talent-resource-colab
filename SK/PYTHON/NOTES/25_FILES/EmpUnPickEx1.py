#Program for Reading The records from file(emp.pick)  by using Un-Pickling.
#EmpUnPickEx1.py
import pickle
def readempvalues():
	try:
		with open("emp.pick","rb") as fp:
			print("----------------------------------------")
			print("\tEmployee Records")
			print("----------------------------------------")
			while(True):
				try:
					record=pickle.load(fp)
					for val in record:
						print("\t{}".format(val),end="  ")
					print()
				except EOFError:
					print("----------------------------------------")
					break
			
	except FileNotFoundError:
		print("File does not Exist")

#Main Program
readempvalues() # Function Call