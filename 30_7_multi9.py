"""activeCount():-to return the no of threads objects currently live"""
import threading
print("welcome")
class x(threading.Thread):
    def run(self):
        print("hello")
class y(threading.Thread):
    def run(self):
        print("kunal")
t1=x()
t1.start()
t2=y()
t2.start()
print(threading.activeCount())
print("bye")
