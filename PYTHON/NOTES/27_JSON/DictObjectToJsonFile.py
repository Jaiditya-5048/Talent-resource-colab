#Program for Saving Dict Object to JSON File
#DictObjectToJsonFile.py
import json

print("---------------------------------------")
dictobj={"eno":100,"name":"Rossum","sal":4.5}
print(dictobj,type(dictobj))
print("---------------------------------------")
#Save the Dict object Data to the JSON File
with open("emp.json","a") as fp:
    json.dump(dictobj,fp)
    print("Dict Data saved in JSON File--verify")