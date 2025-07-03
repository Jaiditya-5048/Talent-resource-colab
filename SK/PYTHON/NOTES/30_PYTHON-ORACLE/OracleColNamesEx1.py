#Program for Obtaining Col Names of Table (Meta-Data)
#OracleColNamesEx1.py
import oracledb as orc
def colnames():
    try:
        con=orc.connect("system/tiger@localhost/orcl")
        cur=con.cursor()
        #Query
        sq="select * from employee"
        cur.execute(sq)
        #To get Col Names along with Its Descriptors
        print("-"*50)
        colinfo=cur.description
        for col in colinfo:
            print(col[0],end="\t")
        print()
        print("-" * 50)
    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)

#Main Program
colnames() # Function Call