#Program for Demonstrating the NEED of Keyword Variable Length Arguments
#PureKeywordVarLengArgsEx5.py
def findtotal(sno,sname,cls,*vals, city="HYD",**submarks):
	print("*"*50)
	print("Number of Variable length args:",len(vals))
	for val in vals:
			print("{}".format(val),end=" ")
	print()
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
findtotal(100,"Kalash","X",1,2,3,4,5,Hindi=90,English=80,Telugu=60,Maths=90,Science=88,Social=98)
findtotal(200,"Rajesh","XII",10,20,30,40,50,60,Sanskrit=90,Eng=80,Physics=60,Chemistry=57,Maths_1A=60,Maths_1B=75)
findtotal(300,"Sai","B.Tech(CSE)",0.2,0.3,0.4,CM=50,CPP=60,PYM=70)
findtotal(400,"TR","Scientist",11,22,33,44,city="NL")
findtotal(500,"JH","Diploma",CGI=30,OS=40,dbms=50,ai=40,city="MUM")
findtotal(cls="Scientist",city="USA",sno=600,sname="JG",m1=60,m2=40,m3=60,m5=70)
findtotal(600,"KVR","Trainer",city="AP")
