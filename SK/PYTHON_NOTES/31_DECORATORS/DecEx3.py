#Program for accepting a Line of Text and get them in words by using decorator
#DecEx3.py
def getlines():
	return(input("Enter a Line of Text:"))

def getwords(GL):
	def processlines():
		line=GL()
		words=line.split()
		return words
	return processlines


#Main Program
PL=getwords(getlines) # Decorator Call
result=PL()
print("Words=",result)



