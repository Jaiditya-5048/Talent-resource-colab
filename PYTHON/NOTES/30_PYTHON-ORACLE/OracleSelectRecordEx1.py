#Program for Reading the Records from Table by using fetchone()
#OracleSelectRecordEx1.py
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
        while(True):
            record = cur.fetchone()
            if(record!=None):
                for val in record:
                    print("{}".format(val),end="\t")
                print()
            else:
                print("-" * 50)
                break
    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)

#Main Program
readrecords()