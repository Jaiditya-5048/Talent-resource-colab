#NameValidation.py<----File Name and Module Name
from NameExcept import InvalidNameError,ZeroSizeError
def validate(name): # name="Guido Va1n Rossum
    words=name.split() # words=["Guido","Va1n","Rossum"]
    if(len(words)==0):
        raise ZeroSizeError
    else:
        res=False
        for word in words:
            if(not word.isalpha()):
                res=True
                break
        if(res):
            raise InvalidNameError
        else:
            return "'{}'is Valid Name".format(name)




