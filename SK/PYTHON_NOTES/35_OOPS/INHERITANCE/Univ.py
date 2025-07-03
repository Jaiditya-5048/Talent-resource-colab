#Univ.py<----File Name and Module Name
class Univ:
    def getunivdet(self):
        self.uname=input("Enter University Name:")
        self.uloc = input("Enter University Location:")
    def dispunivdet(self):
        print("-"*50)
        print("\tUniverisy Name:{}".format(self.uname))
        print("\tUniverisy Location:{}".format(self.uloc))
        print("-" * 50)