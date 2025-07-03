#Program for Searching  all  special symbols  except alphabets and digits
#RegExpr15.py
import re
print("-"*50)
matres=re.finditer("[^A-Za-z0-9]","cA?u4a6DpQ8@bKqP2%LXmR5")
for mat in matres:
	print("start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)