#Program for Mobile Number Validation.
#MobileNumberValidationEx1.py
import re
while(True):
	mno=input("Enter Ur Mobile Number:")
	if(len(mno)==10):
		res=re.search(r"\d{10}",mno)
		if(res!=None):
			print("\t{} is Valid Mobile Number".format(mno))
			break
		else:
			print("\t{} contains non-Int Data--Invalid Type-try again".format(mno))
	else:
		print("\t{} Mobile Number is Invalid Length-try again".format(mno))