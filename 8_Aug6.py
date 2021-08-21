"""
Whenever the multiple threads to acess the same functionality or logics at a time,in that threads are
going to be a critical section

whenever threads are going to be critical section in that case deadlock is occured

-->Deadlock example:
--------------------
"""
import threading
def f1(a):
    print("hello",a,"world")
class x(threading.Thread):
    def run(self):
        f1('python')
class y(threading.Thread):
    def run(self):
        f1("django")
t1=x()
t1.start()
t2=y()
t2.start()

"""in the above example deadlock is occured,
