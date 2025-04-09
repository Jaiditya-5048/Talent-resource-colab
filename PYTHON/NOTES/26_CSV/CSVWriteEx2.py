#Program for adding a Record to the existing CSV File with pythom Code by using csv.writer()
#CSVWriteEx2.py
import csv
records=[800,"Supriya",67.77,"JNTU"]
with open("E:\\KVR-PYTHON-11AM\\CSV\\NOTES\\student.csv","a") as fp:
    csvwr=csv.writer(fp)
    #write the record to the csv file by using writerow()
    csvwr.writerow(records)
    print("Record Added to CSV File  --Verify")




