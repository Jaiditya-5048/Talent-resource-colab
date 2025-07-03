#Program for Generating 1 to n numbers after each every second by using threads
#NumGenEx1.py
import threading, time


def generate(n):
    if (n <= 0):
        print("{}--->{} is Invalid input".format(threading.current_thread().name, n))
    else:
        print("----------------------------------------------")
        print("Numbers within {}".format(n))
        print("----------------------------------------------")
        for val in range(1, n + 1):
            print("{}---Value={}".format(threading.current_thread().name, val))
            time.sleep(0.25)
        print("----------------------------------------------")


#Main Program
t1 = threading.Thread(target=generate, args=(int(input("Enter How Many Number u want to generate:")),))
t1.name = "Generator"
t1.start()
