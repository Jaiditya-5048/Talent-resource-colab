#Program for Deleting the Record from employee table based on employee Number
#OracleDeleteEx1.py
import oracledb as orc
def recorddelete():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        iq="delete from employee where eno=125"
        cur.execute(iq)
        con.commit()
        if(cur.rowcount>0):
            print("{} Employee Record Deleted from employee table".format(cur.rowcount))
        else:
            print("Employee Record Does not Exist")
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#Main Program
recorddelete()