#Program for Creating CSV File with pythom Code  along with Dict data by using csv.writer()
#CSVDictWriteEx1.py
import csv # Step-1
hnames=["PID","PNAME","PRICE"] # Step-2
records=[{"PID":100,"PNAME":"Almond","PRICE":150},
        {"PID":200,"PNAME":"WallNum","PRICE":600},
        {"PID":300,"PNAME":"KIMISS","PRICE":450},
        {"PID":400,"PNAME":"Kikat","PRICE":80},
        {"PID":500,"PNAME":"ChocoPie","PRICE":300}]
with open("E:\\KVR-PYTHON-11AM\\CSV\\NOTES\\product.csv","a") as fp: #step-4
        csvdwr=csv.DictWriter(fp,fieldnames=hnames)
        csvdwr.writeheader()
        csvdwr.writerows(records)
        print("CSV File Created with Dict Data--Verify")



