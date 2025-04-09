#write a python program which will extract  the names and marks from given file(student.data file)--with Reg Expr
#StudentNamesMarksFilesExtractEx.py
import re
with open("E:\\KVR-PYTHON-11AM\\REG EXPR\\NOTES\\student.data","r") as fp:
	filedata=fp.read()
	nameslist=re.findall("[A-Z][a-z]+",filedata)
	markslist=re.findall(r"\d{2}",filedata)
	print("----------------------------------")
	print("\tNmes\t\tMarks")
	print("----------------------------------")
	for names,marks in zip(nameslist,markslist):
		print("\t{}\t\t{}".format(names,marks))
	print("----------------------------------")
