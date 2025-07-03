#Program displaying Vowels from Line of Text
#ContinueStmtEx6.py
nov=0
line=input("Enter a Line of Text:")#line=Apple    ----Python is an oop lang
for ch in line:
    if ch not in ["a","e","i","o","u"]:
        continue
    print(ch)
    nov=nov+1
print("Number of Vowels=",nov)