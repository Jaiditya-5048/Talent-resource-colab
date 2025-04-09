#Program for Reading the Records from Table by using fetchall()
#OracleSelectRecordEx2.py
import oracledb as orc
def readrecords():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        #Query
        sq="select * from employee"
        cur.execute(sq)
        #Process the Records
        print("-"*50)
        print("Employee Details")
        print("-" * 50)
        records=cur.fetchall()
        for record in records:
            for val in record:
                print("{}".format(val),end="\t")
            print()
        print("-" * 50)
    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)

#Main Program
readrecords()