"""enumerate():-to return the list of thread object curreently alive"""
import threading
print("Welcome")
class x(threading.Thread):
    def run(self):
        print("hello")
class y(threading.Thread):
    def run(self):
        print("hey")
t1=x()
t1.start()
t2=y()
t2.start()
print(threading.enumerate())
print("bye")
