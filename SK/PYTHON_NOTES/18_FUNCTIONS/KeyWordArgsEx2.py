#Program for Demonstrating Key Word Args
#KeyWordArgsEx2.py
def  dispvalues(a,b,c,d): # Here a,b,c,d are called Formal parameters
    print("\t{}\t{}\t{}\t{}".format(a,b,c,d))

#Main Program
print("="*50)
print("\tA\tB\tC\tD")
print("="*50)
dispvalues(10,20,30,40) # Function call with Poss Args
dispvalues(c=30,a=10,d=40,b=20) # Function call with Keyword Args
dispvalues(d=40,c=30,b=20,a=10) # Function call with Keyword Args
dispvalues(10,20,d=40,c=30) # Function call with Poss and Keyword Args
#dispvalues(d=40,c=30,10,20)--SyntaxError: positional argument follows keyword argument
print("="*50)