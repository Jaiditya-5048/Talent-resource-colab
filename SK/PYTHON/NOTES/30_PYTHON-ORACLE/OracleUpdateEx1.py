#Program for Updating the Records of employee Table
#OracleUpdateEx1.py
import oracledb as orc
def recordupdate():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        uq="update employee set sal=45.67,compname='MSoft' where eno=175 "
        cur.execute(uq)
        con.commit()
        if(cur.rowcount>0):
            print("{} Employee Record Update from employee table".format(cur.rowcount))
        else:
            print("Employee Record Does not Exist")
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#Main Program
recordupdate()