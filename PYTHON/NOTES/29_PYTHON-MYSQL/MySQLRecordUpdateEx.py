#Program for Updating the Records of employee Table
#MySQLRecordUpdateEx.py
import mysql.connector
def recordupdate():
    while(True):
        try:
            con = mysql.connector.connect(host="127.0.0.1",
                                          user="root",
                                          passwd="root",
                                          database="batch11am")
            cur=con.cursor()
            #Get Emp Number, sal and comp name for updation
            empno=int(input("Enter Employee Number for updating other Details:"))
            empsal=float(input("Enter New Salary of employee:"))
            #Design the Query
            uq="update employee set sal=%f where eno=%d" %(empsal,empno)
            cur.execute(uq)
            con.commit()
            if(cur.rowcount>0):
                print("{} Employee Record Updated from employee table".format(cur.rowcount))
            else:
                print("Employee Record Does not Exist")
            ch = input("Do u want to Update Another record(yes/no):")
            print("--------------------------------------")
            if (ch.lower() == "no"):
                print("Thx for this Program")
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL DB:",db)
        except ValueError:
            print("Don't enter alnums,strs and special symbols for empno and sals-try again")

#Main Program
recordupdate()