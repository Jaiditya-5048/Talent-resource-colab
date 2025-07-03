#Program for Demonstrating the NEED of Keyword Variable Length Arguments
#PureKeywordVarLengArgsEx2.py

def dispvals(**kvr): #Here **kvr is called Kwd Var length param and whse type <class,'dict'>
	print("-----------------------------------------------")
	for key,value in kvr.items():
		print("\t{}--->{}".format(key,value))
	print("-----------------------------------------------")


#Main Program
dispvals(sno=10,sname="RS",cm=40,cppm=60,pym=50)# Function call-1 with 5 Keywords args
dispvals(eno=20,ename="JG",bsal=6000,hra=16) # Function call-2 with 4 Keywords args
dispvals(sid=30,stname="Ramesh",hb1="eating",hb2="sleeping",hb3="chatting",hb4="reels") # Function call-3 with 6 Keywords args
dispvals(cid=40,cname="Rakesh")# Function call-4 with 2 Keywords args
dispvals()