#Program for Demonstrating continue statement.
#ContinueStmtEx4.py
s="PYTHON"
print("By using while loop")
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
else:
    print("else part of for loop")
print("----------------------------------")
#My Requirment is--to display-- PYHN
i=0
while(i<len(s)):
    if(s[i]=="T") or (s[i]=="O"):
        i=i+1
        continue

    print(s[i])
    i=i+1
else:
    print("else part of for loop")
print("----------------------------------")