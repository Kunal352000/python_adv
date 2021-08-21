import threading
print("Welcome")
import time
class x(threading.Thread):
    def run(self):
        for i in range(5):
            print("hai")
class y(threading.Thread):
    def run(self):
        time.sleep(10)
        for j in range(5):
            print("kunal")
t1=x()
t1.start()
t2=y()
t2.start()
for k in range(5):
    print("hello")
