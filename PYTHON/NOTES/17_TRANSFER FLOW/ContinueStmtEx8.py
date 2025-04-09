#Program displaying consonants from Line of Text
#ContinueStmtEx8.py
line=input("Enter a Line of Text:")#line=Apple
for ch in line.lower():
    if ch in ["a","e","i","o","u"," ","0","1","2","3","4","5","6","7","8","9"] :
        continue
    print(ch)