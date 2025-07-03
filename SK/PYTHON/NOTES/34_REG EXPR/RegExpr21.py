#Program for Searching  all  special symbols except  word chars (alphabets + digits)
#RegExpr21.py
import re
print("-"*50)
matres=re.finditer(r"\W","c A?u 4a6DpQ8@bKqP2%LXmR5")
for mat in matres:
	print("start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)