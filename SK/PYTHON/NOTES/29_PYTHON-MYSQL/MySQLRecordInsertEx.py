#Program for Reading Employee Values from KBD and Insert into Employee Table
#MySQLRecordInsertEx.py
import mysql.connector
def recordinsert():
    while(True):
        try:
            con = mysql.connector.connect(host="127.0.0.1",
                                          user="root",
                                          passwd="root",
                                          database="batch11am")
            cur=con.cursor()
            #Accept the employee Values from KBD
            print("--------------------------------------------")
            empno=int(input("Enter Employee Number:"))
            ename=input("Enter Employee Name:")
            sal=float(input("Enter Employee Salary:"))
            print("--------------------------------------------")
            iq="insert into employee values(%d,'%s',%f)" %(empno,ename,sal,)
            cur.execute(iq)
            con.commit()
            print("{} Employee Record Inserted in employee table".format(cur.rowcount))
            print("--------------------------------------------")
            ch=input("Do u want to Insert Another record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for this Program")
                break

        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL DB:",db)
        except ValueError:
            print("Don't enter alnums,strs and special symbols for empno and sals-try again")

#Main Program
recordinsert()