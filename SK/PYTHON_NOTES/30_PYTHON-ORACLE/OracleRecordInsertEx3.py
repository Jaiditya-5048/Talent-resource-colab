#Program for Reading Employee Values from KBD and Insert into Employee Table
#OracleRecordInsertEx2.py
import oracledb as orc
def recordinsert():
    while(True):
        try:
            con=orc.connect("system/tiger@localhost/orcl")
            cur=con.cursor()
            #Accept the employee Values from KBD
            print("--------------------------------------------")
            empno=int(input("Enter Employee Number:"))
            ename=input("Enter Employee Name:")
            sal=float(input("Enter Employee Salary:"))
            cname=input("Enter Employee Comp Name:")
            print("--------------------------------------------")
            iq="insert into employee values(%d,'%s',%f,'%s')" %(empno,ename,sal,cname)
            cur.execute(iq)
            con.commit()
            print("{} Employee Record Inserted in employee table".format(cur.rowcount))
            print("--------------------------------------------")
            ch=input("Do u want to Insert Another record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for this Program")
                break

        except orc.DatabaseError as db:
            print("Problem in Oracle DB:",db)
        except ValueError:
            print("Don't enter alnums,strs and special symbols for empno and sals-try again")

#Main Program
recordinsert()