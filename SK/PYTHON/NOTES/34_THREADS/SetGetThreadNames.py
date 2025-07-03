#Program for Demonstrating setName() and getName() 
#SetGetThreadNames.py
import threading
def welcome():
	print("welcome() executed by {}".format(threading.current_thread().name))


#Create sub threads
t1=threading.Thread(target=welcome) # Here t1 is thread object and whose default name Thread-1
#thname=t1.getName()----here getName() is deprecated (Changed) to the attribute called "name"
thname=t1.name # Getter  Approach
print("Sub Thread Name=",thname)
#set our name to sub thread
#t1.setName("KVR")----here setName() is deprecated (Changed) to the attribute called "name"
t1.name="ROSSUM" # setter  Approach
print("Sub Thread Name=",t1.name)
