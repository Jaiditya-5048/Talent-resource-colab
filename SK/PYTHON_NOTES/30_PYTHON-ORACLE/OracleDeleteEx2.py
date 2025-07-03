#Program for Deleting the Record from employee table based on employee Number
#OracleDeleteEx2.py
import oracledb as orc
def recorddelete():
    while(True):
        try:
            con=orc.connect("system/tiger@localhost/orcl")
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
        except orc.DatabaseError as db:
            print("Problem in Oracle DB:",db)
        except ValueError:
            print("Don't enter Alnums,strs and symbols for emp number-try again")

#Main Program
recorddelete()