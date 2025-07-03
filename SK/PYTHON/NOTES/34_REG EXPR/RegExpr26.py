#Program for Searching   for Zero K or One K 
#RegExpr26.py
import re
print("-"*50)
matres=re.finditer(".","KVKKVKKKVKV")
for mat in matres:
	print("start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

