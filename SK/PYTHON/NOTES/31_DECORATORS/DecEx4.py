#Program for accepting a Line of Text and get them in words by using decorator
#DecEx4.py
def getwords(GL):
	def  processlines():
		line=GL()
		words=line.split()
		return words,len(words)
	return processlines

@getwords            # gere @getwords is called Decorator
def getlines():
	return(input("Enter a Line of Text:"))

#Main Program
words,nowords=getlines() # Normal Function Call
print("Words in the Line=",words)
print("Number of Words=",nowords)
