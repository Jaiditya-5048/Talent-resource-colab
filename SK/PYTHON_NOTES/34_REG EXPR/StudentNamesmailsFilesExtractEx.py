#write a python program which will extract  the names and  mails from given file(studentmails.data file)--with Reg Expr
#StudentNamesmailsFilesExtractEx.py
import re
with open("E:\\KVR-PYTHON-11AM\\REG EXPR\\NOTES\\studentsmails.data","r") as fp:
		filedata=fp.read()
		mailslist=re.findall(r"\S+@\S+",filedata)
		nameslist=re.findall("[A-Z][a-z]+",filedata)
		print("----------------------------------")
		print("\tNames\t\tMails")
		print("----------------------------------")
		for names,mails in zip(nameslist,mailslist):
			print("\t{}\t\t{}".format(names,mails))
		print("----------------------------------")
		
