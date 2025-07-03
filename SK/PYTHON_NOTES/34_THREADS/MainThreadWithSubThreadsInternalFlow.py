#Program for Showing Internal Flow of MainTherad with Sub Threads 
#MainThreadWithSubThreadsInternalFlow.py
import threading
def  welcome():
	print("welcome() executed by: {}".format(threading.current_thread().name))

def  hello():
	print("hello() executed by: {}".format(threading.current_thread().name))
	
def  hi():
	print("hi() executed by: {}".format(threading.current_thread().name))

#Main Program
print("Program Execution Started by:{}".format(threading.current_thread().name)) # MainThread
#create Sub threads
t1=threading.Thread(target=welcome) # here t1 is called sub thread whose name is "thread-1"
t2=threading.Thread(target=hello)  # here t2 is called sub thread whose name is "thread-2"
t3=threading.Thread(target=hi)  # here t3 is called sub thread whose name is "thread-3"
# dispatch the sub threads to execute targetted Functions by using start()
t1.name="RS"
t2.name="TR"
t3.name="DR"
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Program Execution Ended by:{}".format(threading.current_thread().name)) # MainThread

