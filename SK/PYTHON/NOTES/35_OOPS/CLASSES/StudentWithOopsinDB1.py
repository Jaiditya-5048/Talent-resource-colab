#Program for Reading Student Deatils from KeyBoard and Insert Student Deatils in Student table of MySQL
#StudentWithOopsinDB1.py
import mysql.connector
class Student:
	def getStudData(self):
		try:
			self.sno=int(input("Enter Student Number:"))
			self.sname=input("Enter Student Name:")
			self.marks=float(input("Enter Student Marks:"))
		except ValueError:
			print("Don't Enter alnums,strs and symbols for sno and marks")
		else:
			self.savestuddata() # Calling Instance from another Instance Method Same Class

	def savestuddata(self):
		# Python with MySQL Communication Code
		try:
			con=mysql.connector.connect(host="localhost",
																	user="root",
																	passwd="root",
																	database="batch11am")
			cur=con.cursor()
			iq="insert into student values(%d,'%s',%f)"
			cur.execute(iq %(self.sno,self.sname,self.marks))
			con.commit()
			print("Student Record Inserted--Student Table--Verify")
		except mysql.connector.DatabaseError:
			print("Problem in MySQL")
	
#Main Program
s=Student()
s.getStudData()

