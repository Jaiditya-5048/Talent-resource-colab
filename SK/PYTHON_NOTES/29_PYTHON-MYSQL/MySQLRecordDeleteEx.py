#Program for Deleting the Record from employee table based on employee Number
#MySQLRecordDeleteEx.py
import mysql.connector
def recorddelete():
    while(True):
        try:
            con = mysql.connector.connect(host="127.0.0.1",
                                          user="root",
                                          passwd="root",
                                          database="batch11am")
            cur=con.cursor()
            iq="delete from employee where eno=%d" %(int(input("Enter Emp Number to Delete the Record:")))
            cur.execute(iq)
            con.commit()
            if(cur.rowcount>0):
                print("{} Employee Record Deleted from employee table".format(cur.rowcount))
            else:
                print("Employee Record Does not Exist")
            print("--------------------------------------")
            ch = input("Do u want to Delete Another record(yes/no):")
            if (ch.lower() == "no"):
                print("Thx for this Program")
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL DB:",db)
        except ValueError:
            print("Don't enter Alnums,strs and symbols for emp number-try again")

#Main Program
recorddelete()