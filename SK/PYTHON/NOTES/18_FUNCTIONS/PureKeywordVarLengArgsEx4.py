#Program for Demonstrating the NEED of Keyword Variable Length Arguments
#PureKeywordVarLengArgsEx4.py
def findtotal(sno,sname,cls,city="HYD",**submarks):
	print("*"*50)
	print("\tStudent Number:{}".format(sno))
	print("\tStudent Name:{}".format(sname))
	print("\tStudent Class:{}".format(cls))
	print("\tStudent City:{}".format(city))
	if(len(submarks)==0):pass
	else:
		print("-"*50)
		print("\tSubject Name\tMarks")
		print("-"*50)
		totmarks=0
		for subject,marks in submarks.items():
			print("\t{}\t\t{}".format(subject,marks))
			totmarks+=marks
		print("*"*50)
		print("\tTOTAL MARKS={}".format(totmarks))	
	print("*"*50)

#Main Program
findtotal(100,"Kalash","X",Hindi=90,English=80,Telugu=60,Maths=90,Science=88,Social=98)
findtotal(200,"Rajesh","XII",Sanskrit=90,Eng=80,Physics=60,Chemistry=57,Maths_1A=60,Maths_1B=75)
findtotal(300,"Sai","B.Tech(CSE)",CM=50,CPP=60,PYM=70)
findtotal(400,"TR","Scientist","NL")
findtotal(500,"JH","Diploma",CGI=30,OS=40,dbms=50,ai=40,city="MUM")
findtotal(cls="Scientist",city="USA",sno=600,sname="JG",m1=60,m2=40,m3=60,m5=70)
