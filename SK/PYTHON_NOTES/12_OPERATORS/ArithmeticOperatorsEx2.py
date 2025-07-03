#program for Calculating Simple Interest and total amount to pay
#ArithmeticOperatorsEx2.py
#Accepting Input from KeyBoard
p=float(input("Enter Priciple Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate of Interest:"))
#calculate si and totamt
si=(p*t*r)/100
totamt=p+si
#Dsplay the Result
print("="*50)
print("\tRESULTS OF SIMPLE INTEREST")
print("="*50)
print("\tPrinciple Amount:{}".format(p))
print("\tTime:{}".format(t))
print("\tRate of Interest:{}".format(r))
print("\t-----------------------------")
print("\tSIMPLE INTEREST=:{}".format(si))
print("\tTOTAL AMOUNT TO PAY:{}".format(totamt))
print("="*50)
