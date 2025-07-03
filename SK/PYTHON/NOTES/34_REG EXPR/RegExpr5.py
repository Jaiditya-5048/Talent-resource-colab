#Program for Searching  all except  'a' or 'b' or 'c' only
#RegExpr5.py
import re
gd="cAu4a6DpQ8@bKqP2%LXmR5"
sp="[^abc]"
print("-"*50)
matres=re.finditer(sp,gd)
for mat in matres:
	print("start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)