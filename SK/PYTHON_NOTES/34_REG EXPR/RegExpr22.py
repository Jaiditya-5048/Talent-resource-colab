#Program for Searching   Exatcly One K
#RegExpr22.py
import re
print("-"*50)
matres=re.finditer("K","KVKKVKKKVKV")
for mat in matres:
	print("start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)