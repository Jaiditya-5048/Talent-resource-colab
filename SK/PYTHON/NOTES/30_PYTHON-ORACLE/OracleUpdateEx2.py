#Program for Updating the Records of employee Table
#OracleUpdateEx1.py
import oracledb as orc
def recordupdate():
    while(True):
        try:
            con=orc.connect("system/tiger@localhost/orcl")
            cur=con.cursor()
            #Get Emp Number, sal and comp name for updation
            empno=int(input("Enter Employee Number for updating other Details:"))
            empsal=float(input("Enter New Salary of employee:"))
            cname=input("Enter New Comp Name of Employee:")
            #Design the Query
            uq="update employee set sal=%f,compname='%s' where eno=%d " %(empsal,cname,empno)
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
        except orc.DatabaseError as db:
            print("Problem in Oracle DB:",db)
        except ValueError:
            print("Don't enter alnums,strs and special symbols for empno and sals-try again")

#Main Program
recordupdate()