#Program displaying Vowels from Line of Text
#ContinueStmtEx5.py
nov=0
line=input("Enter a Line of Text:")#line=Apple    ----Python is an oop lang
for ch in line.lower():
    if(ch!='a') and (ch!='e') and (ch!='i') and (ch!='o') and (ch!='u'):
        continue
    print(ch)
    nov=nov+1
else:
    print("Number of Vowels=",nov)