#Program for Converting Json String data into Dict Data
#JsonStrDataToDictData.py
import json
print("------------------------------")
jsondata='{"empno":"100","name":"Rossum","Sal":"3.4"}'
print(jsondata,type(jsondata))
print("------------------------------")
#Convert JsonData into Dict Type data
dictobj=json.loads(jsondata)
print(dictobj,type(dictobj))
for k,v in dictobj.items():
    print("\t{}--->{}".format(k,v))
print("------------------------------")