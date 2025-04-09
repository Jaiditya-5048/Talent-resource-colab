#This Program inserts in the records
#StudentInsert.py<---File Name and Module Name
import pickle
class InvalidNameError(Exception):pass

def validatename(name): # name="Guido Va1n Rossum
    words=name.split() # words=["Guido","Va1n","Rossum"]
    if(len(words)==0):
        raise ZeroSizeError
    else:
        res=False
        for word in words:
            if(not word.isalpha()):
                res=True
                break
        if(res):
            raise InvalidNameError
        else:
            return name
def insertrecords():
	with open("student.info","ab") as fp:
		try:
			#read student values
			print("---------------------------------------------------")
			sno=int(input("Enter Student Number:"))
			sname=validatename(input("Enter Student Name:"))
			marks=float(input("Enter Student Marks:"))
			print("---------------------------------------------------")
			#create an empty list for placing student values
			lst=list()
			lst.append(sno)
			lst.append(sname)
			lst.append(marks)
			#save list object data into the file
			pickle.dump(lst,fp)
			print("Student Data Saved Sucessfully in a File:")
		except ValueError:
			print("Don't enter strs, syymbols and alnums for sno and marks--try again")
		except InvalidNameError:
			print("Don't entre the name with digits, special symbols--try again")

