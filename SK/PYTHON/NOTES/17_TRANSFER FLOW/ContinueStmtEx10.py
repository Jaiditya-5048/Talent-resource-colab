#Program displaying special from Line of Text
#ContinueStmtEx10.py
line=input("Enter a Line of Text:")#line=Apple
nosp=0
for ch in line:
    if(ch.isdigit()) or (ch.isalpha() or (ch.isspace())):
        continue
    print(ch)
    nosp=nosp+1
print("Number of Special symbols=",nosp)