#VoterEx2.py
while(True):
    age=int(input("Enter Ur Valid Age:"))
    if(age>=18):
        break
    print("\t\t{} is Invalid Age-try Again".format(age))
print("{} Years Citizen is Eligible to Vote:".format(age))