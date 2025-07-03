#Program for demonstrating the need of generators
#GenEx5.py
def gercrses():
	yield "C"
	yield "C++"
	yield "Java"
	yield "PYTHON"

#Main Program
crs=gercrses() # # Function Call which biuld generator object
print(next(crs))
print(next(crs))
print(next(crs))
print(next(crs))
#print(next(crs))----gives StopIteration

