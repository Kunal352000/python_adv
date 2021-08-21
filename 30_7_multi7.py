#to execute main thread in last//by using join()
import threading
print("hello")
def f1(a):
    print("hello",a,"world")
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
t2.join()
t1.join()
#t2.join()
for i in range(5):
    print("bye")
