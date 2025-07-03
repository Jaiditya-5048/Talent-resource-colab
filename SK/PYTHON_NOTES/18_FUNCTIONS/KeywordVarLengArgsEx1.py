#Program for Demonstrating the NEED of Keyword Variable Length Arguments
#KeywordVarLengArgsEx1.py
#This Program will not execute as it is bcoz PVM is doing Interpretation process and It Remembers only Latest Function Defintion but not all Function definitions with Same Name.
def dispvals(sno,sname,cm,cppm,pym):# Function Def-1
	print(sno,sname,cm,cppm,pym)

def dispvals(eno,ename,bsal,hra): # Function Def-2
	print(eno,ename,bsal,hra)

def dispvals(sid,stname,hb1,hb2,hb3,hb4) : # Function Def-3
	print(sid,stname,hb1,hb2,hb3,hb4)

def dispvals(cid,cname): # Function Def-4
	print(cid,cname)

#Main Program
dispvals(sno=10,sname="RS",cm=40,cppm=60,pym=50)# Function call-1 with 5 Keywords args
dispvals(eno=20,ename="JG",bsal=6000,hra=16) # Function call-2 with 4 Keywords args
dispvals(sid=30,stname="Ramesh",hb1="eating",hb2="sleeping",hb3="chatting",hb4="reels") # Function call-3 with 6 Keywords args
dispvals(cid=40,cname="Rakesh")# Function call-4 with 2 Keywords args