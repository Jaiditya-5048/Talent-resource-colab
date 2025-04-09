#DynamicCSVFileEx1.py
import csv
hn=int(input("Enter How Many Col Names CSV File Contains:"))
if(hn<=0):
    print("{} in valid Input".format(hn))
else:
    hnames=[]
    for i in range(1,hn+1):
        cn=input("Enter {} Col Name:".format(i))
        hnames.append(cn)
    else:
        #print(hnames) # ['TNO', 'TNAME', 'SUB', 'EXP']
        #get the Records
        nor=int(input("Enter How Many Records in CVS  File u want:"))
        if(nor<=0):
            print("{} is Invalid Input".format(nor))
        else:
            records=[] # for Holding Records--outer list
            for recno in range(1,nor+1):
                print("Enter {} Record Values:".format(recno))
                print("--------------------------")
                record=[] # for string single Record--inner list
                for j in range(0,len(hnames)):
                    colval=input("Enter {} Value:".format(hnames[j]))
                    record.append(colval)
                else:
                    records.append(record)
            else:
                #print(records)
                #[['100', 'RS', 'PYTHON'], ['200', 'DR', 'C'], ['300', 'JG', 'Java']]
                csvfile=input("Enter CSV File Name with extension.csv:")
                with open(csvfile,"a") as fp:
                    csvwr=csv.writer(fp)
                    csvwr.writerow(hnames)
                    csvwr.writerows(records)
                    print("CSV File Created dynamically--Verify")
