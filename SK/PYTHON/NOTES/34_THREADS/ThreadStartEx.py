#Program for Demonstrating Thread() and start() and is_alive()
#ThreadStartEx.py
import threading
def welcome():
	print("welcome() executed by {}".format(threading.current_thread().name))

def hello(val):
	print("{}, Good Morning".format(val))
	print("hello() executed by {}".format(threading.current_thread().name))

#Create sub threads
print("------------------------------------------------------------------
t1=threading.Thread(target=welcome)
t2=threading.Thread(target=hello,args=("Rossum",)
print("Is sub thread under execution=",t1.is_alive())
print("Is sub thread under execution=",t2.is_alive())
#dispatch the sub threads
t1.start()
t2.start()
print("Is sub thread under execution=",t1.is_alive())
print("Is sub thread under execution=",t2.is_alive())
