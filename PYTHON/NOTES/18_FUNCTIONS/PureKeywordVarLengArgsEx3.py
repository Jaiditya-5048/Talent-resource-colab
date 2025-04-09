#Program for Demonstrating the NEED of Keyword Variable Length Arguments
#PureKeywordVarLengArgsEx3.py
def findtotal(sno,sname,cls,**submarks):
	print("*"*50)
	print("\tStudent Number:{}".format(sno))
	print("\tStudent Name:{}".format(sname))
	print("\tStudent Class:{}".format(cls))
	if(len(submarks)==0):pass
	else:
		print("-"*50)
		print("\tSubject Name\tMarks")
		print("-"*50)
		totmarks=0
		for subject,marks in submarks.items():
			if(subject!="tm"):
				print("\t{}\t\t{}".format(subject,marks))
				totmarks+=marks
		print("*"*50)
		print("\tTOTAL MARKS Secured / Total Marks={}/{}".format(totmarks,submarks['tm']))	
		print("\tPERCENTAGE={}".format(round((totmarks/submarks['tm'])*100,2)))
	print("*"*50)

#Main Program
findtotal(100,"Kalash","X",Hindi=90,English=80,Telugu=60,Maths=90,Science=88,Social=98,tm=600)
findtotal(200,"Rajesh","XII",Sanskrit=90,Eng=80,Physics=60,Chemistry=57,Maths_1A=60,Maths_1B=75,tm=470)
findtotal(300,"Sai","B.Tech(CSE)",CM=50,CPP=60,PYM=70,tm=300)
findtotal(400,"TR","Scientist")
