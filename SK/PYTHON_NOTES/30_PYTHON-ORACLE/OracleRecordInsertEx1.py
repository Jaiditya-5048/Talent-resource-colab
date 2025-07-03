#Program for Reading Employee Values from KBD and Insert into Employee Table
#OracleRecordInsertEx1.py
import oracledb as orc
def recordinsert():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        iq="insert into employee values(200,'TR',2.5,'PANDAS')"
        cur.execute(iq)
        con.commit()
        print("Employee Record Inserted in employee table")
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#Main Program
recordinsert()