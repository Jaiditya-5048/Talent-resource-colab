#Program for accepting a Line of Text and Convert It into Lower and Upper case by using Decorator
#DecEx6.py
def tolowercase(text):
	def converttolower():
		line,uppercase=text()
		lowercase=line.lower()
		return line,uppercase,lowercase
	return converttolower

def toppercase(text):
	def converttoupper():
			line=text()
			uppercase=line.upper()
			return line,uppercase
	return converttoupper

@tolowercase
@toppercase
def getText():
	return input("Enter a Line of Text:")


#Main Program
text,upcasetext,lowertext=getText()
print("-------------------------------------------------------")
print("Given Text:{}".format(text))
print("Upper Case:{}".format(upcasetext))
print("Lower Case:{}".format(lowertext))
print("-------------------------------------------------------")