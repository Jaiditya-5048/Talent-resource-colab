#Program for Mobile Number Validation.
#MobileNumberValidationEx2.py
import re
while(True):
	mno=input("Enter Ur Mobile Number:")
	if(len(mno)==10):
		res=re.search(r"[98]\d{8}",mno)
		if(res!=None):
			print("\t{} is Valid Mobile Number".format(mno))
			break
		else:
			print("\t{} contains non-Int Data / must starts with the combition of 98--Invalid Type-try again".format(mno))
	else:
		print("\t{} Mobile Number is Invalid Length-try again".format(mno))