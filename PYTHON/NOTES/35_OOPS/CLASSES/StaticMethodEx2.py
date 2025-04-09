#Program for Demonstrating the need of Static Method
#StaticMethodEx2.py
class Arithmetic:
	def readValues(self):
		self.a=float(input("Enter First Value:"))
		self.b=float(input("Enter Second Value:"))
		self.op=input("Enter Any Arithmetic Operator:")

class Calc:
	@staticmethod
	def  arithmeticoperation(obj):  # obj.__dict__ = {'a': 30.0, 'b': 20.0, 'op': '**'}
		match(obj.op):
			case "+":
				print("sum({},{})={}".format(obj.a,obj.b,obj.a+obj.b))
			case "-":
				print("sub({},{})={}".format(obj.a,obj.b,obj.a-obj.b))
			case "*":
				print("mul({},{})={}".format(obj.__dict__['a'],obj.__dict__['b'],obj.__dict__['a']*obj.__dict__['b']))
			case "/":
				print("Div({},{})={}".format(obj.__dict__['a'],obj.__dict__['b'],obj.__dict__['a']/obj.__dict__['b']))
			case "//":
				print("FloorDiv({},{})={}".format(obj.__dict__.get('a'),obj.__dict__.get('b'),obj.__dict__.get('a')//obj.__dict__.get('b')))
			case "%":
				print("ModDiv({},{})={}".format(obj.__dict__['a'],obj.__dict__['b'],obj.__dict__['a']%obj.__dict__['b']))
			case "**":
				print("Pow({},{})={}".format(obj.a,obj.b,obj.a**obj.b))
			case _:
				print("{} is Not an Arithmetic Operator".format(obj.op))
		

#Main Program
ao=Arithmetic()
ao.readValues()
#Perform Arithmetic Operation
Calc.arithmeticoperation(ao)