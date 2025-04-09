#Program for Searching  all   except alphabets
#RegExpr13.py
import re
print("-"*50)
matres=re.finditer("[^A-Za-z]","cAu4a6DpQ8@bKqP2%LXmR5")
for mat in matres:
	print("start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)