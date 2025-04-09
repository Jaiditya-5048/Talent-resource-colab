#Program for Demonstrating "Every Python Program contains Thread"
#MainThreadEx1.py
import threading 
tname=threading.current_thread().name
print("Default Name of therad=",tname) # MainThread
print("Number of threads by default=",threading.active_count()) # 1