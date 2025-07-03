#StudentSearch.py<----File Name and Module Name
import pickle
def studentsearch():
	try:
		studlist=[]
		with open("student.info","rb") as fp:
			while(True):
				try:
					record=pickle.load(fp)
					studlist.append(record)
				except EOFError:
					break
			#accept stud number for view perticular student details
			found=False
			stno=int(input("Enter Student Number to Search the Details:"))
			for indexval in range(0,len(studlist)):
				if(studlist[indexval][0]==stno):
					found=True
					recindex=indexval
					break
			print("-----------------------------------------")
			if(found):
				print("Single Student Information")
				print("-----------------------------------------")
				for val in studlist[recindex]:
					print(val,end="\t")
				print()
			else:
				print("Record does not Exist")
			print("-----------------------------------------")
	except FileNotFoundError:
		print("File does not Exist")