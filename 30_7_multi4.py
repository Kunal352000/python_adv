"""we can suspend thread execution temporary some time by using sleep function
of time module"""
import threading
print("Welcome")
import time
class x(threading.Thread):
    def run(self):#userThread
        for i in range(5):
            print("hey")
class y(threading.Thread):
    def run(self):#userThread
        time.sleep(3.2)
        for j in range(5):
            print("kunal")
t1=x()
t1.start()
t2=y()
t2.start()
for k in range(5):#mainThread
    print("hello")
