#Digits.py
dobj={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
d=int(input("Enter a Digit:"))
res=dobj.get(d) if dobj.get(d)!=None  else "-Ve Digit " if (-9<=d<0) else "Number"
print("{} is {}".format(d,res))
