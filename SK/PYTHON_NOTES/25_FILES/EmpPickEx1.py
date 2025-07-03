#Program for Reading The Values of employee and save them in file(emp.pick)  by using Pickling.
#EmpPickEx1.py
import pickle
def  saveempvalues():
	with open("emp.pick","ab") as fp:
		#read emp values
		print("---------------------------------------------------")
		eno=int(input("Enter Employee Number:"))
		ename=input("Enter Employee Name:")
		sal=float(input("Enter Employee Salary:"))
		print("---------------------------------------------------")
		#create an empty list for placing emp values
		lst=list()
		lst.append(eno)
		lst.append(ename)
		lst.append(sal)
		#save list object data into the file
		pickle.dump(lst,fp)
		print("Emp Data Saved Sucessfully in a File:")

#Main Program
saveempvalues() # Function Call

	
