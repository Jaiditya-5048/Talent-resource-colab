#Program for Searching   for Zero K or One K or More K's
#RegExpr24.py
import re
print("-"*50)
matres=re.finditer("K*","KVKKVKKKVKV")
for mat in matres:
	print("start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

