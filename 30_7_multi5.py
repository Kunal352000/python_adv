#deadlock
import threading
def f1(a):
    print("Hello",a,"world")
class x(threading.Thread):
    def run(self):
        f1("python")
class y(threading.Thread):
    def run(self):
        f1("django")
t1=x()
t1.start()
t2=y()
t2.start()
