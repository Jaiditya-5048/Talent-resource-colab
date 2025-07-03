#write a python program which will extract  the names and marks from given file(student.data file)--without Reg Expr
#StudentNamesMarksFilesExtractEx1.py
import re
with open("E:\\KVR-PYTHON-11AM\\REG EXPR\\NOTES\\student.data","r") as fp:
		filedata=fp.read()
		words=filedata.split()
		#extract the names
		nameslist=[]
		for word in words:
			if(word[0].isupper()):
				nameslist.append(word)
		#extract the marks
		markslist=[]
		for word in words:
			if(len(word)==2) and (word.isdigit()):
				markslist.append(word)
		print("----------------------------------")
		print("\tNames\t\tMarks")
		print("----------------------------------")
		for names,marks in zip(nameslist,markslist):
			print("\t{}\t\t{}".format(names,marks))
		print("----------------------------------")
