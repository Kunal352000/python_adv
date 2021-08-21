import threading
def f1(a):
    print("hello",a,"world")
lock_obj=threading.Lock()
class x(threading.Thread):
    def run(self):
        lock_obj.acquire()
        f1("python")
        lock_obj.release()
class y(threading.Thread):
    def run(self):
        lock_obj.acquire()
        f1('django')
        lock_obj.release()
t1=x()
t1.start()
t2=y()
t2.start()
