#Program for Demonstrating Global and Local Variables
#GlobalLocalVarEx1.py
def  learnAI():
	sub1="AI"  # Here sub1 is called Local Variable
	print("To develop '{}' Based Applications, we use '{}' Lang".format(sub1,lang))
	#print(sub2,sub3)----Can't access bcoz sub2 and sub3 are local in Other functions
		
def learnML():
	sub2="ML"  # Here sub2 is called Local Variable
	print("To develop '{}' Based Applications, we use '{}' Lang".format(sub2,lang))
	#print(sub1,sub3)----Can't access bcoz sub1 and sub3 are local in Other functions

def learnDL():
	sub3="DL" # Here sub3 is called Local Variable
	print("To develop '{}' Based Applications, we use '{}' Lang".format(sub3,lang))
	#print(sub1,sub1)----Can't access bcoz sub1 and sub2 are local in Other functions

#Main Program
lang="PYTHON" # Here lang is called Global Variable
learnAI()
learnML()
learnDL()