#Program for Reading Json File Data into Dict Object
#JsonFileDataToDictData.py
import json
try:
    with open("emp.json","r") as fp:
        object=json.load(fp)
        print(object,type(object))
    print("----------------------------------------")
    for k,v in object.items():
        print("{}-->{}".format(k,v))
    print("----------------------------------------")
except FileNotFoundError:
    print("File does not Exist")