#Program for Demonstrating the NEED of Keyword Variable Length Arguments
#KeywordVarLengArgsEx2.py
#This Program will  execute as it is 
def dispvals(sno,sname,cm,cppm,pym):# Function Def-1
	print(sno,sname,cm,cppm,pym)

dispvals(sno=10,sname="RS",cm=40,cppm=60,pym=50)# Function call-1 with 5 Keywords args
#---------------------------------------------------------------------------------
def dispvals(eno,ename,bsal,hra): # Function Def-2
	print(eno,ename,bsal,hra)

dispvals(eno=20,ename="JG",bsal=6000,hra=16) # Function call-2 with 4 Keywords args
#---------------------------------------------------------------------------------
def dispvals(sid,stname,hb1,hb2,hb3,hb4) : # Function Def-3
	print(sid,stname,hb1,hb2,hb3,hb4)

dispvals(sid=30,stname="Ramesh",hb1="eating",hb2="sleeping",hb3="chatting",hb4="reels") # Function call-3 with 6 Keywords args
#---------------------------------------------------------------------------------
def dispvals(cid,cname): # Function Def-4
	print(cid,cname)

dispvals(cid=40,cname="Rakesh")# Function call-4 with 2 Keywords args
#---------------------------------------------------------------------------------


#NOTE: Accorinf to the above Program
# If we have n-Number of Family Simlar Function calls then we Must Define N-Number of Function definitions 
# This Procees is Time Consuming and Lots of Development time is waste
# We are looking For ONE FUNCTION DEFINITION for n-Number of Family Simlar Function calls--done by Keyword Variable Length Args
