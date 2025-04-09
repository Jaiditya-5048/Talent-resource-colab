#Program for Showing Internal Flow of MainTherad (Default Thread only).
#MainThreadInternalFlow.py
import threading
def  welcome():
	print("welcome() executed by: {}".format(threading.current_thread().name))

def  hello():
	print("hello() executed by: {}".format(threading.current_thread().name))
	
def  hi():
	print("hi() executed by: {}".format(threading.current_thread().name))

#Main Program
print("Program Execution Started by:{}".format(threading.current_thread().name)) # MainThread
welcome() # Function Call-1
hello()  # Function Call-2
hi() # Function Call-3
print("Program Execution Ended by:{}".format(threading.current_thread().name)) # MainThread

